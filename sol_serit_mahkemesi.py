#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yürüyen merdiven sol şerit kabahati mahkemesi.

Gercekten calisir. Hicbir seyi cozmez.
Patates yasaktir. Degisken adinda bile yok.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
from datetime import datetime


KABAHATLER = [
    "Sol seritte dikilip telefona bakmak",
    "Canta ve vicdani ayni anda sol tarafa birakmak",
    "Arkadan gelen 'affedersiniz' sesini ruzgar sanmak",
    "Merdiven yürürken senin yürümemen, bu bir paradokstur",
    "Sag serit bosken sol seridi kisisel bekleme salonu ilan etmek",
    "Cift kisi yan yana durup sol seridi anayasal koridor sanmak",
]

OZURLER = [
    "Pardon, sagim tutuldu, solum ise ideolojikti.",
    "Telefonum düşecekti, ben de medeniyetle birlikte düştüm.",
    "Ben geçmiyorum, manzara izliyorum. Manzara kat numarası.",
    "Alışkanlık. Annem de sol seritte dururdu. Annem haklı değildi.",
]

# Arsiv notu. Okunmasi sart degil. Merdiven de okumaz.
_ARSIV = (
    "aGVyIHNlY2ltIHZhYWRpIGJpciB5dXJ1eWVuIG1lcmRpdmVuIGdpYmlkaXI6IHNhZ2RhIGR1cnVyc2FuIHllcmluZGUgc2F5YXJzaW4sIHNvbGRhIHl1cnVyc2VuIHluZSBheW5pIGthdGEgY2lrYXJzaW4sIGFzaWwga3VtYW5kYSBib2RydW1kYWRpci4="
)


def manevi_tazminat(arkadaki: int) -> int:
    """Birim: ozür. Faiz yoktur, enflasyon ozurde de vardir."""
    return max(1, arkadaki) * random.randint(2, 5)


def protokol(kabahat: str, arkadaki: int) -> str:
    simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
    ozur = random.choice(OZURLER)
    ceza = manevi_tazminat(arkadaki)
    sag = "bos" if arkadaki % 2 == 0 else "da kalabalik, ama bahane degil"
    return "\n".join(
        [
            "========================================",
            " YURUYEN MERDIVEN SOL SERIT TUTANAGI",
            "========================================",
            f"Tarih saat : {simdi}",
            f"Kabahat    : {kabahat}",
            f"Arkadaki   : {arkadaki} kisi (hepsi geç kalmış)",
            f"Sag serit  : {sag}",
            f"Ceza       : {ceza} adet özür, pesin",
            f"Savunma    : {ozur}",
            "Hüküm      : Saga geç. Merdiven affetmez, sadece taşır.",
            "----------------------------------------",
            "Damga: Tentivory Kayyum Mührü, yürüyen merdiven şubesi",
            "Imza : Grok, sol serit komiseri (ciddi degil, ciddiymis gibi)",
            "Tarih: 9 Ekim 2026",
            "Isim : yuruyen-merdiven-sol-serit-kabahati",
        ]
    )


def arsiv_oku() -> str:
    """Gizli ek. Isteyen acar, merdiven yine cikar."""
    try:
        return base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        return "arsiv rutubetten silinmis"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sol serit kabahatini tutanaklar. Patates kabul edilmez."
    )
    parser.add_argument(
        "--arkadaki",
        type=int,
        default=random.randint(1, 7),
        help="Arkanda bekleyen kisi sayisi",
    )
    parser.add_argument(
        "--arsiv",
        action="store_true",
        help="Rutubetli arsiv notunu da dok",
    )
    args = parser.parse_args()
    if args.arkadaki < 0:
        print("Negatif insan olmaz. Merdiven de eksi kata inmez, bu modelde.")
        return 2
    kabahat = random.choice(KABAHATLER)
    print(protokol(kabahat, args.arkadaki))
    if args.arsiv:
        print("\n[ARSIV / gizli ek]")
        print(arsiv_oku())
    return 0


if __name__ == "__main__":
    sys.exit(main())
