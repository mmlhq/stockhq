from pytdx.hq import TdxHq_API

api = TdxHq_API()
if api.connect('119.147.212.81',7709):
    print("ok")
    data = api.get_security_bars(9, 0, '000001', 0, 10) #返回普通list
    data = api.to_df(api.get_security_bars(9, 0, '000001', 0, 10)) # 返回DataFrame
    print(data)

    api.disconnect()


