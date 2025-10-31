def evaluate_result(result):
    a, b, c = result
    if a == b == c:
        return f"🎉 中獎啦！{a} 三連發！"
    elif a == b or b == c or a == c:
        return "💖 XX耀等你啦，加油"
    else:
        return "😢 看來皇上晚上得自己來了"