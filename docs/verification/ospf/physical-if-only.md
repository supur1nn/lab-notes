# OSPF を物理 IF だけで有効にしたとき

!!! info "検証中"
    設定と確認コマンドの出力までは記録済み。仮説と考察はこれから書く。進め方は [検証の進め方](../workflow.md) を参照。

- 開始日：2026-10-23（[勉強記録](../../study-log/2026-10-23.md)）
- 前の検証：[OSPF をループバックだけで有効にしたとき](loopback-only.md)（ネイバーが張れず、ループバックは広報されなかった）
- 構成・設定・確認コマンドの出力は、CML の MCP サーバーから取得した

## 問い

**IOS XR で、OSPF を物理 IF（R1 と R2 をつなぐ G0/0/0/0）だけで有効にしたとき、どうなるのか。**

- ネイバーは張れるか
- 何が広報されるか
- ループバックは広報されるか

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

（試す前に考えたことを書く）

## 設定

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

## 確認

### インターフェース

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

### OSPF

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

## 結果

（何が起きたか、仮説どおりだったかを書く）

## 考察

（なぜその結果になったかを書く）

## 次の問い

（考察から出てきた疑問を書く）
