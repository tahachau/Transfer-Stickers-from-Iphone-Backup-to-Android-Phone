import os
import shutil
from PIL import Image  # Pillow library

# Paths
BACKUP_PATH = r"D:\Apple Computer\MobileSync\Backup\00008110-001202840EEB801E"
FILELIST_PATH = r"C:\Users\Ironnix\Downloads\sticker_fileIDs.txt"  # text file with fileIDs pasted
OUTPUT_PATH = r"C:\Users\Ironnix\Documents\stickers verified"
LOG_PATH = os.path.join(OUTPUT_PATH, "conversion_log.txt")

def extract_and_convert_stickers():
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

    success, failed, animated = [], [], []

    # Read fileIDs from text file
    with open(FILELIST_PATH, "r") as f:
        fileIDs = [line.strip() for line in f if line.strip()]

    for fileID in fileIDs:
        subfolder = fileID[:2]
        src = os.path.join(BACKUP_PATH, subfolder, fileID)
        if os.path.exists(src):
            temp_webp = os.path.join(OUTPUT_PATH, fileID + ".webp")
            shutil.copy(src, temp_webp)

            try:
                # Open with context manager to ensure file is closed
                with Image.open(temp_webp) as img:
                    if getattr(img, "is_animated", False):
                        # Keep animated stickers as webp
                        animated.append(fileID)
                        # Just leave the copied .webp in OUTPUT_PATH
                    else:
                        # Convert static stickers to PNG
                        img = img.convert("RGBA")
                        png_path = os.path.join(OUTPUT_PATH, fileID + ".png")
                        img.save(png_path, "PNG")
                        os.remove(temp_webp)
                        success.append(fileID)
            except Exception:
                failed.append(fileID)
                # Clean up bad file
                if os.path.exists(temp_webp):
                    os.remove(temp_webp)

    # Write log
    with open(LOG_PATH, "w") as log: # type: ignore
        log.write("Static stickers converted to PNG:\n")
        log.write("\n".join(success) + "\n\n")
        log.write("Animated stickers kept as WEBP:\n")
        log.write("\n".join(animated) + "\n\n")
        log.write("Failed conversions:\n")
        log.write("\n".join(failed))

    print(f"Converted {len(success)} static stickers to PNG")
    print(f"Kept {len(animated)} animated stickers as WEBP")
    print(f"{len(failed)} files skipped. See conversion_log.txt for details.")

if __name__ == "__main__":
    extract_and_convert_stickers()