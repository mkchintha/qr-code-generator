from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H


def is_valid_url(url: str) -> bool:
    """Basic URL validation without extra packages."""
    try:
        parts = urlparse(url)
        return parts.scheme in ("http", "https") and bool(parts.netloc)
    except Exception:
        return False


def generate_qr(
    url: str,
    out_path: Path,
    error: str = "M",
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
) -> Path:
    """Create and save a QR image for the given URL."""
    ec_map = {
        "L": ERROR_CORRECT_L,
        "M": ERROR_CORRECT_M,
        "Q": ERROR_CORRECT_Q,
        "H": ERROR_CORRECT_H,
    }

    qr = qrcode.QRCode(
        version=None,  # auto size based on content
        error_correction=ec_map.get(error.upper(), ERROR_CORRECT_M),
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)

    # Open in the default image viewer for a screenshot like the assignment sample
    try:
        img.show(title="img")
    except Exception:
        pass

    return out_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="QR Code generator for URLs")
    parser.add_argument("-u", "--url", help="URL to encode. If omitted, you will be prompted.")
    parser.add_argument("--ec", choices=["L", "M", "Q", "H"], default="M", help="Error correction level")
    parser.add_argument("--box-size", type=int, default=10, help="Pixels per QR module")
    parser.add_argument("--border", type=int, default=4, help="Quiet zone width, in modules")
    parser.add_argument("-o", "--output", help="Output PNG path. Default is output/qr_<timestamp>.png")

    args = parser.parse_args()

    url = args.url or input("Enter a URL: ").strip()
    if not is_valid_url(url):
        raise SystemExit("Invalid URL. Include http:// or https:// and a valid host.")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = Path(args.output) if args.output else Path("output") / f"qr_{ts}.png"

    saved = generate_qr(
        url=url,
        out_path=out_file,
        error=args.ec,
        box_size=args.box_size,
        border=args.border,
    )
    print(f"Saved QR to: {saved.resolve()}")