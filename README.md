[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/sendycrypto67-lgtm/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/sendycrypto67-lgtm/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
# The World Today: Sunday 22 November 2026

A one-image newspaper front page summing up the world news of Sunday
22 November 2026, built for the make.fun bounty
[news-image-20261122](https://make.fun/bounty/news-image-20261122)
("Sum up 22 November's world news in one image").

The image is a cream broadsheet page, masthead **THE WORLD TODAY**,
dated **SUNDAY 22 NOVEMBER 2026**, with six stories in a 3 by 2 grid.
Each story has a flat editorial illustration, a red topic tag, a bold
headline and a one-line sub-caption. The six stories were verified
against real reporting from 21-22 November 2026 (AP, Reuters, USGS,
Financial Times). No casualty figures appear anywhere in the image.

## The six stories

1. **CLIMATE TALKS RUN INTO OVERTIME** (Climate) - COP31 in Antalya,
   Turkey, ran past its scheduled Friday close with no final deal, as
   the draft agreement left out any mention of fossil fuels.
2. **STRONG QUAKE SHAKES PERU'S ANDES** (Peru) - A powerful earthquake
   struck the central Andes near Junin on Friday evening, was felt in
   Lima, and had no damage reported at first.
3. **DRONES HIT RUSSIAN SHIP IN THE BALTIC** (Baltic) - Drones hit the
   Russian cargo vessel Sparta II in the Gulf of Finland on Saturday
   morning; the ship caught fire and drifted toward Finnish waters.
4. **MEXICO CAPTURES TOP CARTEL BOSS** (Mexico) - Mexican forces
   captured Fausto Isidro Meza Flores, known as "El Chapo Isidro" and
   one of the FBI's most wanted, in Sinaloa with help from US
   intelligence.
5. **WASHINGTON PUSHES UKRAINE PEACE DEAL** (Ukraine) - The US pressed
   Ukraine and Russia toward a peace agreement by early January, with
   NATO-style security guarantees for Ukraine back in the talks.
6. **US STOCKS SLIDE AS AI RALLY FADES** (Markets) - US shares fell
   sharply on Friday as the AI sell-off deepened; the Nasdaq erased
   its 2026 gains and entered correction territory.

## How main.py works

`main.py` is Python 3, standard library only. It finds `entry.png`
next to itself and validates it: PNG magic bytes, an IHDR chunk of
length 13 with non-zero dimensions of at most 1024 on each side, a
file size of at most 1048576 bytes, and an IEND chunk at the end of
the file (four zero length bytes, then `IEND`, then four CRC bytes).
It then copies the file byte for byte to `$MAKEFUN_OUTPUT_DIR` (or
`/output` when unset), re-reads the copy, and asserts that the copy's
sha256, size and dimensions equal the source's. On success it prints
the source path, dimensions, byte size, sha256 and destination; on
failure it exits 1 with an error naming the file. No network, no
randomness, so both runs write identical bytes.

## How to run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` - the front page image, 1024x1024, 567511 bytes,
  sha256 `416a510037341a3b2edf1be8fa8a0b0d74beeb3c5fd295f4fb4d866a704ee3b3`
- `main.py` - validator and copier described above
- `README.md` - this file
- `LICENSE` - MIT license
- `BUILD_LOG.md` - research, generation and test notes

Referral: https://make.fun/r/y8skhesk
