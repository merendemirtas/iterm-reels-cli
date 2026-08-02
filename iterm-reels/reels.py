import os
import shutil
import subprocess
import sys

REELS_FILE = "reels.txt"

def clear_screen():
    """Terminal ekranını ve tampon geçmişini temizler."""
    print("\033c", end="")

def load_reels(file_path):
    """reels.txt dosyasından Reels linklerini okur."""
    if not os.path.exists(file_path):
        print(f"[!] Hata: '{file_path}' dosyası bulunamadı.")
        print(f"[+] Lütfen '{file_path}' dosyası oluşturup linkleri ekleyin.")
        sys.exit(1)
        
    with open(file_path, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
    if not links:
        print(f"[!] Hata: '{file_path}' dosyasında geçerli link bulunamadı.")
        sys.exit(1)
        
    return links

def get_terminal_geometry():
    """iTerm2 pencere boyutuna göre timg çözünürlüğünü dinamik ayarlar."""
    columns, lines = shutil.get_terminal_size((80, 24))
    width = max(40, int(columns * 0.75))
    height = max(20, int(lines * 0.75))
    return f"{width}x{height}"

def play_stream():
    reels_list = load_reels(REELS_FILE)
    loop_count = 1
    
    while True:
        for index, url in enumerate(reels_list, start=1):
            clear_screen()
            geom = get_terminal_geometry()
            
            print("=" * 60)
            print(f" 🎬 iTerm2 Reels CLI | Tur: #{loop_count} | Video: {index}/{len(reels_list)}")
            print(" 🕹️  [ENTER] -> Sonraki Video | [q + ENTER] -> Çıkış")
            print("=" * 60 + "\n")
            
            cmd = f'exec yt-dlp -q --no-warnings -o - "{url}" 2>/dev/null | timg -V -p iterm2 -g {geom} - 2>/dev/null'
            
            process = subprocess.Popen(
                cmd,
                shell=True,
                preexec_fn=os.setsid
            )
            
            try:
                user_input = input()
            except (KeyboardInterrupt, EOFError):
                user_input = 'q'
                
            try:
                os.killpg(os.getpgid(process.pid), 9)
            except Exception:
                pass

            if user_input.strip().lower() == 'q':
                clear_screen()
                print("👋 Reels akışı kapatıldı.")
                sys.exit(0)
                
        loop_count += 1

if __name__ == "__main__":
    try:
        play_stream()
    except Exception as e:
        print(f"\n[!] Hata oluştu: {e}")