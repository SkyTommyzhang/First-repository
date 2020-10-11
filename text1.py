import ybc_carbrand as cb
import ybc_box as box
import ybc_pic_search as ps


box.msgbox('汽车品牌大全')
# 使用brands()功能获取汽车品牌,存入变量res
res = cb.brands()
choice = box.buttonbox('汽车类型',res)
if choice != None:
    choice = choice + '汽车'
    picsearch.pic_search(choice)
    files = os.listdir(choice)
    for filename in files:
        filename = choice + '/' + filename
        # 使用msgbox()展示图片
        box.msgbox('王德发：真香哎',filename)
else:
    box.msgbox('请选择汽车类型！')