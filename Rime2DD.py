#-*-coding:utf-8-*-
'''
本程序用以将不知郑码的码表转换为多多郑码的码表。
转换原则非常简单：
一\ta\tav 一\ta
𩸎\trwd 𩸎\trwd
其实说白了，就是将原不知郑码码表中每行第二项之后的项全部去除。（否则多多输入法会将其全部纳入，如“一”的编码会变成'aav'，从而造成错误。）
'''

input_f1 = './Input/bzzm.words.dict'
input_f2 = './Input/bzzm.phrases.dict'
input_f3 = './Input/bzzm.symbols.dict'

output_f1 = input_f1.replace('Input','Output') + '.forDD.txt'
output_f2 = input_f2.replace('Input','Output') + '.forDD.txt'
output_f3 = input_f3.replace('Input','Output') + '.forDD.txt'

def read_input_file_to_list(from_file_path):
    '''
    此函數用以讀入欲比较之文件。將文件每行内容存爲一个【列表】。
    '''
    result = ''
    with open(from_file_path, 'r', encoding = 'utf-8') as f:
        result = f.readlines() #讀入文檔的全部內容並存爲字符串
    return result

def write_into_file(to_file_path, s):
    with open(to_file_path, 'w', encoding = 'utf-8') as f:
        f.write(s)

def transfer(list_x):
    result = []
    for line_single in list_x:
        line_single = line_single.replace('\n', '') #先把每行末的\n给替换掉
        items = line_single.split('\t')
        result.append(items[0]+'\t'+items[1])
    return result

if __name__ == '__main__':
    r1 = transfer(read_input_file_to_list(input_f1))
    r2 = transfer(read_input_file_to_list(input_f2))
    r3 = transfer(read_input_file_to_list(input_f3))

    result1 = '\n'.join(r1)
    result2 = '\n'.join(r2)
    result3 = '\n'.join(r3)

    write_into_file(output_f1, result1)
    write_into_file(output_f2, result2)
    write_into_file(output_f3, result3)
    #print (result1)
