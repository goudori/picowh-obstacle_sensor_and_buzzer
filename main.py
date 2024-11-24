import machine  # type: ignore
import utime  # type: ignore

# ピンの設定
buzzer = machine.Pin(15, machine.Pin.OUT)  # ブザーのピン
ir_sensor = machine.Pin(18, machine.Pin.IN)  # 赤外線センサーのピン

while True:
    # 障害物を検知している場合
    if ir_sensor.value() == 0:  # センサー出力が 0 のとき障害物あり
        for i in range(1):  # 1回音を鳴らす
            buzzer.value(1)  # ブザーをON
            utime.sleep(0.3)  # 0.3秒待機
            buzzer.value(0)  # ブザーをOFF
            utime.sleep(0.3)  # 0.3秒待機
        utime.sleep(1)  # 次のループ前に少し待機
    else:
        # 障害物がない場合、ブザーを鳴らさない
        buzzer.value(0)
        utime.sleep(0.1)  # 状態確認のための短い待機
