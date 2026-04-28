"""Frame extraction from rendered video using ffmpeg.

The judge needs visual evidence to score, so we extract N evenly-spaced
keyframes from the rendered video. Higgsfield outputs are 4–15s, so 4
frames is enough to capture the hook, mid, and resolution.
"""

from __future__ import annotations

import base64
import os
import shutil
import subprocess
from pathlib import Path

import httpx


def _ffmpeg_bin() -> str:
    bin_path = os.environ.get("FFMPEG_BIN") or shutil.which("ffmpeg")
    if not bin_path:
        raise RuntimeError(
            "ffmpeg not found on PATH. Install it (apt/brew install ffmpeg) "
            "or set FFMPEG_BIN."
        )
    return bin_path


def download_video(video_url: str, dest_dir: Path) -> Path:
    """Download a video URL to local disk and return the path."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "video.mp4"
    with httpx.stream("GET", video_url, follow_redirects=True, timeout=120.0) as r:
        r.raise_for_status()
        with dest.open("wb") as f:
            for chunk in r.iter_bytes(chunk_size=64 * 1024):
                f.write(chunk)
    return dest


def extract_keyframes(video_path: Path, dest_dir: Path, n: int = 4) -> list[Path]:
    """Extract N evenly-spaced JPG keyframes from a video.

    Uses ffmpeg's `select` filter to pick frames at fractional duration
    points (1/(n+1), 2/(n+1), ..., n/(n+1)).
    """
    dest_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg = _ffmpeg_bin()

    duration = _probe_duration(video_path)
    timestamps = [duration * (i + 1) / (n + 1) for i in range(n)]

    paths: list[Path] = []
    for i, ts in enumerate(timestamps):
        out = dest_dir / f"frame_{i + 1:02d}.jpg"
        cmd = [
            ffmpeg,
            "-y",
            "-loglevel", "error",
            "-ss", f"{ts:.3f}",
            "-i", str(video_path),
            "-frames:v", "1",
            "-q:v", "3",
            str(out),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        paths.append(out)
    return paths


def _probe_duration(video_path: Path) -> float:
    """Return video duration in seconds via ffprobe."""
    ffprobe = shutil.which("ffprobe") or _ffmpeg_bin().replace("ffmpeg", "ffprobe")
    out = subprocess.run(
        [
            ffprobe,
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(video_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(out.stdout.strip())


def frame_to_image_block(frame_path: Path) -> dict:
    """Convert a JPG frame to a Claude API image content block."""
    data = base64.standard_b64encode(frame_path.read_bytes()).decode("ascii")
    return {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": data,
        },
    }
