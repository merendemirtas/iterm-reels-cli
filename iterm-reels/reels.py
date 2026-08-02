import os
import subprocess
import sys

reels_list = [
    "https://www.instagram.com/reel/DbEB0l_i90Z/",
    "https://www.instagram.com/reel/DbgJBmjOdn1/",
    "https://www.instagram.com/reel/DbiPrAXIBae/"
]

def clear_screen():
    # Terminal ekranını ve geçmiş tamponu tamamen temizler
    print("\033c", end="")

def main():
    for index, url in enumerate(reels_list, start=1):
        clear_screen()
        print(f"==================== REELS {index}/{len(reels_list)} ====================")
        print(" [ENTER] -> Sonraki Video | [q + ENTER] -> Çıkış")
        print("========================================================\n")
        
        # yt-dlp ve timg çıktılarını tam sessiz moda alıyoruz
        cmd = f'exec yt-dlp -q --no-warnings -o - "{url}" 2>/dev/null | timg -V -p iterm2 -g 70x35 - 2>/dev/null'
        
        # Süreci bağımsız süreç grubunda başlat (kill edince tamamen kapansın)
        process = subprocess.Popen(
            cmd,
            shell=True,
            preexec_fn=os.setsid
        )
        
        try:
            user_input = input()
        except (KeyboardInterrupt, EOFError):
            user_input = 'q'
            
        # Enter'a basıldığı an tüm video/grafik süreçlerini öldür
        try:
            os.killpg(os.getpgid(process.pid), 9)
        except Exception:
            pass

        if user_input.strip().lower() == 'q':
            clear_screen()
            print("Reels akışı kapatıldı.")
            sys.exit(0)

    clear_screen()
    print("Listendeki tüm videolar bitti!")

if __name__ == "__main__":
    main()