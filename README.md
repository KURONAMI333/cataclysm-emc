# ProjectE: EMC for L_Ender's Cataclysm

> Lets L_Ender's Cataclysm's materials enter ProjectE's transmutation system. Without this add-on, ProjectE cannot price any of them.

[![License: All Rights Reserved](https://img.shields.io/badge/License-All%20Rights%20Reserved-lightgrey.svg)](LICENSE)

---

## Why EMC for Cataclysm?

L_Ender's Cataclysm の素材は ProjectE からは「値の付かない未知のアイテム」で、賢者の石を持っていても変換テーブルに載らない。この MOD は Cataclysm の金属・ボス素材・遺跡装飾・音楽ディスクに EMC 値を与える data-only アドオンで、中身は変換定義 JSON 1本（Java コードなし）。手付けしたのは 1.21.1 で 56 id、1.20.1 で 69 id。残りはホスト自身のバニラ型レシピを ProjectE が辿って自動導出する。

---

## Features

- ⚖️ **金属の値は進行順どおり** — black steel 288 < ancient metal 1152 < ignitium 2304 < witherite 2560 < cursium 3072 < enderite block 9216。掘るより高いが、討伐報酬として割に合う帯に揃えてある
- 🧱 **インゴットにだけ値を置く** — ナゲットとブロックは通常クラフト経由で整数導出（9の倍数設計なので往復完全等価）。Cataclysm に鉱石ブロックは存在しないので、「別の形から安く刷る」抜け穴は構造的に無い
- 🗿 **ボス素材は討伐の対価** — 召喚アイテム（各ボスの eye）のコストと戦利品の期待値を8ボス全員で数値検証済み。Ancient Remnant と The Harbinger だけは労働対価として利益側（2.46x / 2.18x）を意図的に受理している
- 💿 **音楽ディスクは9枚とも 2,048** — 1.21.1 の ProjectE はディスクタグに値を持たないため全枚手付け。1.20.1 は ProjectE 側のタグ値がそのまま効くので触らない
- 🔮 **紫水晶の祭壇も対応** — Blessed Amethyst Crab Meat への変換は独自レシピ型のため ProjectE に見えない。触媒なしの1:1等価として明示定義した
- 🚫 **道具・武器・防具・装飾品は敢えて EMC 無し** — vanilla 同様、クラフト可能な装備品はレシピから導出させ、耐久やエンチャントという state を変換で消さないため
- 🧩 **サーバー側だけで動く** — 配布物はデータ jar のみ。クライアントへの導入は不要

---

## Installation

1. **NeoForge（Minecraft 1.21.1）** または **Forge（Minecraft 1.20.1）** を導入
2. 必須のホスト MOD を導入: [ProjectE](https://www.curseforge.com/minecraft/mc-mods/projecte) と [L_Ender's Cataclysm](https://modrinth.com/mod/l_enders-cataclysm)
3. `cataclysm_emc-0.1.0+neoforge-1.21.1.jar`（NeoForge 1.21.1）または `cataclysm_emc-0.1.0+forge-1.20.1.jar`（Forge 1.20.1）をサーバーの `mods/` フォルダに放り込む

---

## Configuration

この MOD に設定項目は無い。値はすべてデータパック形式の変換定義で、入れた瞬間から有効になる。

---

## Compatibility

動作確認は次の組み合わせで実施済み（dedicated server で EMC 計算が完走・parse エラー 0）:

| Minecraft | Loader | Cataclysm | ProjectE |
|---|---|---|---|
| 1.21.1 | NeoForge | 3.33 | PE 1.1.0 |
| 1.20.1 | Forge | 3.31 | PE 1.0.1 |

1.21.1 セルでは Cataclysm 側の必須依存（lionfishapi、curios）が揃っている必要がある。

---

## FAQ

**Q. 一部のアイテムの EMC が 0 なのはバグ？**  
A. いいえ。スラブ2種（stone tile slab / polished end stone slab）は半分個の計算結果が 1 未満になるため 0 になります。vanilla のスラブと同じ位置づけの正常系です。

**Q. 武器や防具に EMC を付けないのは？**  
A. 意図的です。装備品は耐久値やエンチャントを持つ stateful なアイテムで、EMC 変換がその状態を消したり複製したりすべきではないからです。クラフト可能なものは ProjectE がレシピから自動導出します。

**Q. ボスを倒すと EMC がお得すぎることはある？**  
A. Ancient Remnant（2.46x）と The Harbinger（2.18x）は討伐の手間に対する対価として利益側になるよう設計しています。召喚アイテムは買えますが、多段階のボス戦そのものは省けません。

**Q. クライアントにも入れないといけない？**  
A. 不要です。EMC 値はサーバー側で計算・同期されるデータで、この MOD 自体に Java コードはありません。

---

## Bug Reports / Feature Requests

GitHub Issues に投げてください: [Issues](https://github.com/KURONAMI333/cataclysm-emc/issues)

---

## License

[All Rights Reserved](LICENSE) — modpack への同梱は自由（許可・クレジット不要）。単体での再配布と改変版の配布は不可。ソースは読めるように公開しています。

---

## Credits

- Author: KURONAMI
- Host: [L_Ender's Cataclysm](https://modrinth.com/mod/l_enders-cataclysm) by L_Ender（MCL_Ender）— アセットの権利は MCL_Ender が保持（all rights reserved）、ソースコードは LGPL v3.0。本アドオンはホストのアセットを一切同梱せず、id 文字列と数値のみを含みます
- [ProjectE](https://www.curseforge.com/minecraft/mc-mods/projecte) — EMC システム本体
