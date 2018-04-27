#3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用
#这个列表打印消息，邀请这些人来与你共进晚餐。
nameList = ['xiaowang','xiaoliu','xiaojiang','xiaohei']
print("邀请你们来共进晚餐");
print(nameList)

#3-5 修改嘉宾名单： 你刚刚的值有位嘉宾无法赴约，因此需要另外邀请一位嘉宾
#修改xiaoliu 为 xiaobai
nameList[1] = 'xiaobai'
print(nameList)

#3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
nameList.insert(0, 'xiaohong')
nameList.insert(0, 'xiaotan')
nameList.append('xiaonan')
print(nameList)

#3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
#保留xiaohong 和 xiaohei 嘉宾 其余删除
print("抱歉，无法邀请你来共进晚餐"+nameList.pop(0));
print("抱歉，无法邀请你来共进晚餐"+nameList.pop(1));
print("抱歉，无法邀请你来共进晚餐"+nameList.pop(1));
print("抱歉，无法邀请你来共进晚餐"+nameList.pop(1));
print("抱歉，无法邀请你来共进晚餐"+nameList.pop(2));
print("最后邀请嘉宾名单")

print("邀请"+nameList[0]+"共进晚餐");
print("邀请"+nameList[1]+"共进晚餐");
del nameList[0]
del nameList[0]
print("清空邀请嘉宾列表")
print(nameList)