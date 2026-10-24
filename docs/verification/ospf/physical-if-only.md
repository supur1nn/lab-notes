# OSPF を物理 IF だけで有効にしたとき

!!! info "検証中"
    ステップ①は結果と考察まで記録済み。ステップ②は R1 側（②-a）まで確認済み。進め方は [検証の進め方](../workflow.md) を参照。

- 開始日：2026-10-23（[勉強記録](../../study-log/2026-10-23.md)）
- 前の検証：[OSPF をループバックだけで有効にしたとき](loopback-only.md)（ネイバーが張れず、ループバックは広報されなかった）
- 構成・設定・確認コマンドの出力は、CML の MCP サーバーから取得した

## 問い

**IOS XR で、物理 IF に OSPF を設定したとき、どんな経路が広報されるのか。**

2段階で試す。

| ステップ | OSPF を有効にする IF | PC 側（G0/0/0/1） |
| --- | --- | --- |
| ① | R1-R2 間（G0/0/0/0）だけ | 入れない |
| ② | R1-R2 間（G0/0/0/0）＋ PC 向け（G0/0/0/1） | 入れる |

## 構成

前の検証と同じラボ（CML-Personal 上の IOS XRv 9000 2台と Desktop 2台）。

![ラボ構成図](../../assets/images/2026-10-23-ospf-lab-topology.png)

| リンク | ネットワーク | 接続 |
| --- | --- | --- |
| desktop-1 - R1 | 192.168.1.0/24 | desktop-1 eth1（.1） - R1 G0/0/0/1（.2） |
| R1 - R2 | 192.168.2.0/24 | R1 G0/0/0/0（.1） - R2 G0/0/0/0（.2） |
| R2 - desktop-0 | 192.168.3.0/24 | R2 G0/0/0/1（.2） - desktop-0 eth1（.1） |

| ルータ | ノード | OSPF ルータ ID | Loopback0 |
| --- | --- | --- | --- |
| R1 | IOS XRv 9000 26.1.1 | 1.1.1.1 | 1.1.1.1 |
| R2 | IOS XRv 9000 26.1.1 | 2.2.2.2 | 2.2.2.2 |

## 仮説

| ステップ | 仮説 |
| --- | --- |
| ① ルータ間だけ | ネイバーは張れるが、PC 向けの IP アドレス（192.168.1.0/24、192.168.3.0/24）は広報されない |
| ② ルータ間＋PC 向け | ネイバーが張れて、192.168.1.0/24 や 192.168.3.0/24 の経路が広報される |

- 理由はまだわからない（結果を見てから考察で考える）
- ステップ②で R1・R2 の Router LSA に増えるリンクは、**スタブネットワーク**だと思う。desktop-0・desktop-1 の先には、どこにも行けないから

## ステップ①：ルータ間だけ

### 設定

前の検証から、Loopback0 を OSPF から外し、**G0/0/0/0 だけ**を OSPF に入れた。`network point-to-point` も付けている。

=== "R1"

    ```
    RP/0/RP0/CPU0:iOS-XR-R1#show run router ospf
    router ospf 1
     router-id 1.1.1.1
     area 0
      interface GigabitEthernet0/0/0/0
       network point-to-point
      !
     !
    !
    ```

=== "R2"

    ```
    RP/0/RP0/CPU0:iOS-XR-R2#show run router ospf
    router ospf 1
     router-id 2.2.2.2
     area 0
      interface GigabitEthernet0/0/0/0
       network point-to-point
      !
     !
    !
    ```

### 確認

#### インターフェース

=== "R1"

    ```
    RP/0/RP0/CPU0:iOS-XR-R1#show ipv4 interface brief
    Interface                      IP-Address      Status          Protocol Vrf-Name
    Loopback0                      1.1.1.1         Up              Up       default
    MgmtEth0/RP0/CPU0/0            unassigned      Shutdown        Down     default
    GigabitEthernet0/0/0/0         192.168.2.1     Up              Up       default
    GigabitEthernet0/0/0/1         192.168.1.2     Up              Up       default
    GigabitEthernet0/0/0/2         unassigned      Shutdown        Down     default
    （G0/0/0/3〜8 は unassigned / Shutdown のため省略）
    ```

=== "R2"

    ```
    RP/0/RP0/CPU0:iOS-XR-R2#show ipv4 interface brief
    Interface                      IP-Address      Status          Protocol Vrf-Name
    Loopback0                      2.2.2.2         Up              Up       default
    MgmtEth0/RP0/CPU0/0            unassigned      Shutdown        Down     default
    GigabitEthernet0/0/0/0         192.168.2.2     Up              Up       default
    GigabitEthernet0/0/0/1         192.168.3.2     Up              Up       default
    GigabitEthernet0/0/0/2         unassigned      Shutdown        Down     default
    （G0/0/0/3〜8 は unassigned / Shutdown のため省略）
    ```

#### OSPF

```
RP/0/RP0/CPU0:iOS-XR-R1#show ospf neighbor

Neighbors for OSPF 1

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2         1     FULL/  -        00:00:33    192.168.2.2     GigabitEthernet0/0/0/0
    Neighbor is up for 01:01:54

Total neighbor count: 1
```

```
RP/0/RP0/CPU0:iOS-XR-R1#show route ospf

% No matching routes found
```

```
RP/0/RP0/CPU0:iOS-XR-R2#show route ospf

% No matching routes found
```

```
RP/0/RP0/CPU0:iOS-XR-R1#show ospf database

            OSPF Router with ID (1.1.1.1) (Process ID 1)

		Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
1.1.1.1         1.1.1.1         1901        0x80000008 0x0052e1 2
2.2.2.2         2.2.2.2         1899        0x80000008 0x00f13d 2
```

| コマンド | 出力からわかる事実 |
| --- | --- |
| `show ospf neighbor` | R1 は 2.2.2.2（R2）と **FULL** になっている |
| `show route ospf` | R1・R2 とも、OSPF で学んだ経路は**なし** |
| `show ospf database` | Router LSA が 1.1.1.1 と 2.2.2.2 の **2つ**。どちらも Link count は 2 |

#### Router LSA の中身

R2 の Router LSA（`show ospf database router` の一部）。

```
LS Type: Router Links
Link State ID: 2.2.2.2
Advertising Router: 2.2.2.2
 Number of Links: 2

  Link connected to: another Router (point-to-point)
   (Link ID) Neighboring Router ID: 1.1.1.1
   (Link Data) Router Interface address: 192.168.2.2
    Number of TOS metrics: 0
     TOS 0 Metrics: 1

  Link connected to: a Stub Network
   (Link ID) Network/subnet number: 192.168.2.0
   (Link Data) Network Mask: 255.255.255.0
    Number of TOS metrics: 0
     TOS 0 Metrics: 1
```

#### ルータ間のネットワーク（192.168.2.0/24）

- `show route ospf` には出てこないが、`show route` では **Connected（`C`）** として載っている

## ステップ②：ルータ間＋PC 向け

②は2回に分けて進める。

| | R1 G0/0/0/1（desktop-1 側） | R2 G0/0/0/1（desktop-0 側） |
| --- | --- | --- |
| ②-a | **OSPF を有効化** | まだ入れない |
| ②-b | 有効 | **OSPF を有効化** |

### ②-a：R1 の desktop-1 側だけ有効化

#### 設定

R1 だけに、PC 向けの G0/0/0/1 を追加した（R2 はステップ①のまま）。

```
RP/0/RP0/CPU0:iOS-XR-R1#show run router ospf
router ospf 1
 router-id 1.1.1.1
 area 0
  interface GigabitEthernet0/0/0/0
   network point-to-point
  !
  interface GigabitEthernet0/0/0/1
  !
 !
!
```

#### 確認

```
RP/0/RP0/CPU0:iOS-XR-R1#show ospf interface brief

Interface          PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Gi0/0/0/0          1     0               192.168.2.1/24     1     P2P   1/1
Gi0/0/0/1          1     0               192.168.1.2/24     1     DR    0/0
```

```
RP/0/RP0/CPU0:iOS-XR-R1#show ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2         1     FULL/  -        00:00:37    192.168.2.2     GigabitEthernet0/0/0/0

Total neighbor count: 1
```

```
RP/0/RP0/CPU0:iOS-XR-R2#show route ospf

O    192.168.1.0/24 [110/2] via 192.168.2.1, 00:01:21, GigabitEthernet0/0/0/0
```

```
RP/0/RP0/CPU0:iOS-XR-R1#show route ospf

% No matching routes found
```

R2 から見た R1 の Router LSA（`show ospf database router 1.1.1.1`、一部）。

```
  LS Type: Router Links
  Link State ID: 1.1.1.1
  Advertising Router: 1.1.1.1
  LS Seq Number: 80000004
   Number of Links: 3

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 2.2.2.2
     (Link Data) Router Interface address: 192.168.2.1

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 192.168.2.0
     (Link Data) Network Mask: 255.255.255.0

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 192.168.1.0
     (Link Data) Network Mask: 255.255.255.0
```

| コマンド | 出力からわかる事実 |
| --- | --- |
| `show ospf interface brief`（R1） | OSPF が有効な IF が **2つ**に増えた。G0/0/0/1 の State は **DR**、ネイバー数は **0/0** |
| `show ospf neighbor`（R1） | ネイバーは R2 の1つのまま |
| `show route ospf`（R2） | **192.168.1.0/24 を `O` で学習**（`[110/2]`、次は 192.168.2.1） |
| `show route ospf`（R1） | OSPF の経路は**なし**のまま |
| R1 の Router LSA | Number of Links が **2 → 3**。増えたのは **Stub Network 192.168.1.0/24**。Seq も上がった |

### ②-b：R2 の desktop-0 側も有効化

（これから）

## 結果

| ステップ | 何が起きたか | 仮説どおりか |
| --- | --- | --- |
| ① ルータ間だけ | ネイバーは張れた（FULL）が、PC 向けのネットワーク（192.168.1.0/24、192.168.3.0/24）は広報されなかった | 仮説どおり |
| ②-a R1 の PC 側だけ | R2 が 192.168.1.0/24 を OSPF で学習した。R1 の LSA にはスタブネットワークが1つ増えた | （書く） |
| ②-b R2 の PC 側も | （これから） | （書く） |

## 考察

### ステップ①

- ネイバーは張れているのに、PC 向けのネットワークは広報されていない
- このことから、**OSPF は、OSPF を有効にした IF の経路だけを広報する**のではないかと考えた
- たとえば R1 に PC が複数台つながっていて、PC1 側の IF では OSPF を有効にし、PC2 側の IF では有効にしていない場合、**有効にした PC1 側の IP アドレスの経路だけが広報される**はず
- Router LSA の **Number of Links** は、はじめは「そのルータから見て何台とつながっているか（R2 なら R1 と desktop-0）」だと思った
    - 実際に R2 の LSA を読むと、2つのリンクは「**別のルータ（R1、point-to-point）**」と「**スタブネットワーク（192.168.2.0/24）**」だった。desktop-0 は入っていない
    - つまり、つながっている台数ではなく、**OSPF を有効にした IF について書かれたリンクの数**だった
- 192.168.2.0/24 は、`show route` では Connected として出てくる
    - 同じネットワークを Connected と OSPF の両方で知っているときは、**AD 値が低い方**が選ばれる。だから Connected（`C`）が載り、`O` は載らない
    - `show route 192.168.2.0/24` で確かめると、Connected の AD 値は **0** だった

### ステップ②

（書く）

## 次の問い

（考察から出てきた疑問を書く）

## 補足・アドバイス

!!! tip "自分で確かめてみよう"
    答えは書かず、考えるための手がかりと、やってみると良いことを書いています。

### 考察の言葉づかい

- 「OSPF を有効化した **IF から広報された経路** のみを広報する」と書きかけていたので、少し整理しておくと良さそう。OSPF が広報しているのは、**誰かから届いた経路**なのか、**その IF 自身が持っているネットワーク**なのか。R1 の G0/0/0/1 が持っているネットワークは何か、`show ipv4 interface brief` の IP アドレスとマスクから考えてみよう

### やってみよう

1. **地図の中身を見る**：`show ospf database router` で、R1 と R2 の Router LSA に何が書かれているか見てみよう。Link count が 2 の「2つ」は何と何か。ステップ②のあとで、どこが増えるか比べてみよう
2. **ルータ間のネットワークはどう見えるか**：192.168.2.0/24 は OSPF を有効にした IF のネットワークなのに、`show route ospf` には出てこなかった。`show route` （ospf を付けない）で 192.168.2.0/24 が何として載っているか見てみよう。考察の「有効にした IF の経路だけを広報する」と矛盾しないか考えてみよう
3. **PC1・PC2 の例を本当に試す**：考察で書いた例は、そのまま検証できる。R1 の空いている IF（G0/0/0/2 など）に Desktop をもう1台つないで、片方だけ OSPF を有効にしてみよう
4. **PC 側の IF で OSPF を有効にすると、何が起きるか**：ステップ②のあと、PC 側の IF で `show ospf interface GigabitEthernet0/0/0/1` を見てみよう。PC は OSPF をしゃべらないのに、R1 は PC に向けて何かを送っていないか。送っているなら、それは困ることか。`passive` というキーワードを調べてみよう
5. ✅ **Number of Links の「2」をもう一度読む**（考察に反映済み）：貼ってくれた R2 の Router LSA には `Link connected to:` が2つある。1つ目と2つ目は、それぞれ**何**とつながっていると書いてあるか。その中に desktop-0（192.168.3.0/24）は出てくるか。考察の「何台とつながっているか」と合っているか、読み比べてみよう。ステップ②のあとで、同じ R2 の LSA の Number of Links と `Link connected to:` がどう変わるかも見てみよう
6. ✅ **同じネットワークが2つの方法で知られているとき**（考察に反映済み）：192.168.2.0/24 は R1・R2 とも Router LSA に入っているのに、ルーティングテーブルでは `O` ではなく `C` になった。同じ宛先を Connected と OSPF の両方で知っているとき、ルータはどちらを選ぶのか。`show route 192.168.2.0/24` で出てくる数字や、「アドミニストレーティブディスタンス」を調べてみよう
7. **Connected と OSPF の AD 値は、具体的にいくつか**（Connected は 0 と確認済み）：`show route 192.168.2.0/24` の `[ ]` の中の数字を見てみよう。Connected の数字は R1 のどこで確かめられるか。もし R1 で G0/0/0/0 を `shutdown` したら、192.168.2.0/24 はルーティングテーブルでどうなると思うか（予想してから試そう）
8. ⏸ **1本の線なのに、なぜリンクが2つなのか**（いったん保留）：R1 と R2 は1本のケーブルでつながっているのに、R2 の LSA には「別のルータ」と「スタブネットワーク」の2つが書かれていた。それぞれは、相手の**誰**を、または**何**を伝えているのか。`network point-to-point` を外して（ブロードキャストに戻して）同じ LSA を見ると、リンクの書き方はどう変わるか試してみよう
9. ✅ **「スタブネットワーク」とは**（予想を仮説に記入済み）：ステップ②で PC 向けの IF を OSPF に入れたら、R1 の LSA に増えるリンクは「別のルータ」と「スタブネットワーク」のどちらになると思うか。予想を書いてから確かめよう
10. **スタブかどうかを決めているのは何か**：予想の理由は「desktop の先にはどこにも行けないから」だった。では、desktop-0 の代わりに **OSPF を設定していないルータ**（その先にさらにネットワークがある）をつないだら、R2 の LSA ではスタブネットワークになるか、別のルータになるか。逆に、その先のルータで OSPF を有効にしたらどうなるか。「先に行けるか」と「先に OSPF のルータがいるか」のどちらで決まっているのか考えてみよう
11. **②-a の今、PC 同士は通信できるか**：R2 は 192.168.1.0/24 を知った。では desktop-1 から `ping 192.168.3.1` は通るか。行きと帰りに分けて、R1 と R2 がそれぞれ相手の PC 側のネットワークを知っているか、ルーティングテーブルで確かめてから予想しよう（②-b の前に試すと、違いがよくわかる）
12. **`[110/2]` の2つの数字**：R2 の `show route ospf` の `[110/2]` は、それぞれ何を表しているか。110 は⑦の答えにもなる。2 はどこから来たのか、`show ospf interface brief` の Cost の列と、R1 の LSA の Metrics を足し算してみよう
13. **G0/0/0/1 の State が「DR」**：desktop-1 側の IF は、ネイバーが 0 なのに DR になっている。ルータ間の G0/0/0/0 は P2P だった。この違いはどこから来たか（設定を見比べよう）。DR とは何をする役か、④の `passive` とあわせて調べてみよう
