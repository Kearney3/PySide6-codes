def signal_emitter(slot_function, extra_param):
    # 调用槽函数，并传递额外的参数
    slot_function(extra_param)

def slot_receiver(param):
    print(f"Slot received: 参数1：{param}")

# 使用 lambda 函数传递额外参数
extra_info = "额外参数"
signal_emitter(lambda param: slot_receiver(f"{param}, 参数2：{extra_info}"), "这是参数1")
print('*'*30)
f1 = lambda param: slot_receiver(f"{param}, {extra_info}"), "Hello from signal"
# signal_emitter(slot_receiver, "Hello from signal")
print(f1)
print(f1[1])
print(f1[0])
f1[0]('sad')
