import keyboard
import time


def charged_jump(charged_time):
    print(f"{charged_time}초 차징 점프")

    keyboard.press("space")
    time.sleep(charged_time)
    keyboard.release("space")

    print(f"점프 완료 {charged_time}초")


def step_jump_contrller():
    keyboard.add_hotkey("q", lambda: charged_jump(0.1))
    keyboard.add_hotkey("w", lambda: charged_jump(0.2))
    keyboard.add_hotkey("e", lambda: charged_jump(0.3))
    keyboard.add_hotkey("a", lambda: charged_jump(0.4))
    keyboard.add_hotkey("s", lambda: charged_jump(0.5))
    keyboard.add_hotkey("d", lambda: charged_jump(0.6))
    keyboard.add_hotkey("f", lambda: charged_jump(0.45))
    keyboard.add_hotkey("g", lambda: charged_jump(0.33))
    keyboard.add_hotkey("h", lambda: charged_jump(0.35))


if __name__ == "__main__":
    step_jump_contrller()
    try:
        keyboard.wait("esc")
    except KeyboardInterrupt:
        print("\n 종료")
    print("종료")
