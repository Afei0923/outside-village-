"""Chinese Greeting Module - 中文问候模块"""


def greet(name=None):
    """Generate a Chinese greeting.

    Args:
        name: Optional name to greet. If None, returns a generic greeting.

    Returns:
        A Chinese greeting string.
    """
    if name:
        return f"你好，{name}！欢迎来到村外！"
    return "你好！欢迎来到村外！"


if __name__ == "__main__":
    print(greet())
    print(greet("朋友"))
