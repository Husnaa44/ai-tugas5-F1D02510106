import json
import os

def main():
    if not os.path.exists("kb_sampah.json"):
        print("File kb_sampah.json tidak ditemukan!")
        return

    with open("kb_sampah.json", "r", encoding="utf-8") as file:
        kb = json.load(file)

    print("=" * 50)
    print(kb["judul"])
    print("=" * 50)

    aturan = kb["aturan"]

    semua_maka = [r["maka"] for r in aturan]
    fakta_dasar = []

    for r in aturan:
        for s in r["jika"]:
            if s not in semua_maka and s not in fakta_dasar:
                fakta_dasar.append(s)

    print("\nJawab pertanyaan dengan y (ya) atau t (tidak).")
    memori = []

    for i, fakta in enumerate(fakta_dasar, 1):
        while True:
            jawab = input(
                f"{i}. Apakah sampah memiliki ciri '{fakta}'? (y/t) > "
            ).strip().lower()

            if jawab == "y":
                memori.append(fakta)
                break
            elif jawab == "t":
                break
            else:
                print("Masukkan jawaban y atau t!")

    print("\nFakta awal:", memori if memori else "Tidak ada")

    jejak_alasan = {}
    siklus = 1

    print("\n--- Proses Forward Chaining ---")

    while True:
        aturan_baru = False

        for r in aturan:
            hasil = r["maka"]
            syarat = r["jika"]

            if hasil not in memori:
                cocok = False

                if r["mode"] == "dan":
                    cocok = all(s in memori for s in syarat)
                elif r["mode"] == "atau":
                    cocok = any(s in memori for s in syarat)

                if cocok:
                    memori.append(hasil)

                    pemicu = [s for s in syarat if s in memori]

                    jejak_alasan[hasil] = {
                        "id": r["id"],
                        "pemicu": pemicu,
                        "sumber": r["sumber"]
                    }

                    print(f"Siklus {siklus}: {r['id']} -> {hasil}")

                    aturan_baru = True
                    siklus += 1
                    break

        if not aturan_baru:
            print(f"Siklus {siklus}: tidak ada aturan baru, selesai.")
            break

    semua_syarat = [s for r in aturan for s in r["jika"]]

    kesimpulan = [
        f for f in memori
        if f not in fakta_dasar and f not in semua_syarat
    ]

    print("\n" + "=" * 50)

    if kesimpulan:
        print("Kesimpulan:", "; ".join(kesimpulan))
        print("\nAlasan (Jejak Aturan):")

        daftar_hasil = list(jejak_alasan.keys())
        daftar_hasil.reverse()

        for hasil in daftar_hasil:
            if hasil in kesimpulan or any(
                hasil in r["jika"]
                for r in aturan if r["maka"] in kesimpulan
            ):
                info = jejak_alasan[hasil]
                print(
                    f"- {hasil} <- {info['id']} "
                    f"({', '.join(info['pemicu'])}) "
                    f"[{info['sumber']}]"
                )
    else:
        print("Kesimpulan: Tidak ada kategori sampah yang cocok.")
        print("Alasan: Syarat aturan belum terpenuhi.")

    print("\nCatatan Batas Keberlakuan:")
    print(kb["batas"])
    print("=" * 50)


if __name__ == "__main__":
    main()
