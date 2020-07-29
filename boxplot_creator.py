import matplotlib.gridspec as gridspec
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def config():
    notch = False
    
    with open("./config.txt", "r") as reader:
        config = reader.readlines()

    for c in config:
        if c == "\n":
            continue
        splited = c.split("=")
        typ = splited[0].rstrip().lstrip()
        setting= splited[1].rstrip().lstrip().replace("\n", "")
        if typ == "filepath":
            filepath = setting
        elif typ == "top_name":
            top_name = setting
        elif typ == "bottom_name":
            bottom_name = setting
        elif typ == "box_name":
            box_name = setting
        elif typ == "top_values":
            top_values = setting.split(" ")
        elif typ == "bottom_values":
            bottom_values = setting.split(" ")
        elif typ == "box_values":
            box_values = setting.split(" ")
        elif typ == "variables_value":
            variables_value = setting
        elif typ == "notch":
            if setting == "False":
                notch = False
        elif typ == "title":
            title = setting
        elif typ == "size":
            size = setting
    
    check = verify_config(filepath, top_name, bottom_name,
                          box_name, top_values, bottom_values,
                          box_values, variables_value, size)
    if check:
        return filepath, top_name, bottom_name, box_name, top_values, bottom_values, box_values, variables_value, notch, title, size
    else:
        print("프로그램 종료")
        exit()
                
            
def verify_config(filepath, top_name, bottom_name, box_name,
                 top_values, bottom_values, box_values,
                 variables_value, size):
    check_list = ["filepath", "top_name", "bottom_name", "box_name",
                 "top_values", "bottom_values", "box_values",
                 "variables_value"]
    
    if size != "22" and size != "222":
        print("size는 22 또는 222여야 함")
        return False

    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print("csv 파일의 위치가 잘못됨")
        raise

    for i, check in enumerate([filepath, top_name, bottom_name,
                               box_name, top_values, bottom_values,
                               box_values, variables_value]):
        if check == "":
            if i == 1 and size == "22":
                continue
                
            else:
                print(check_list[i], "가 입력되지 않음")
                return False
            
        elif check == [""]:
            if i == 4 and size == "22":
                continue
        
        if i == 1 or i == 2 or i ==3 or i == 7:
            try:
                test = df[check]
            except KeyError:
                print(check, "는 올바른 컬럼 이름이 아님.")
                raise
                    
        elif i == 4 or i == 5 or i == 6:
            if len(check) != 2:
                print(check_list[i], "는 반드시 공백으로 구분되는 2개의 값이어야함")
                return False
    return True

def flatten(l):
    return  [item for sublist in l for item in sublist]

def to_array(df): # from dataframe to np array
    return np.asarray(flatten(df))


def return_conditional_values_222(df, variables): # returning values for boxplot
    top = variables["names"]["top"]
    bottom = variables["names"]["bottom"]
    box = variables["names"]["box"]
    
    variable_value = variables["variables_value"]
    first_col_name = top
    first_micro1 = variables[first_col_name][0]
    first_micro2 = variables[first_col_name][1]
    
    second_col_name = bottom
    second_micro1 = variables[second_col_name][0]
    second_micro2 = variables[second_col_name][1]
    
    third_col_name = box
    third_micro1 = variables[third_col_name][0]
    third_micro2 = variables[third_col_name][1]
    
    print("""
    2 by 2 by 2 plot data summary:
    
    top name = {}
    bottom name = {}
    box name = {}
    
    variable_value = {}
    
    first_col_name = {}
        first_micro1 = {}
        first_micro2 = {}
    
    second_col_name = {}
        second_micro1 = {}
        second_micro2 = {}
    
    third_col_name = {}
        third_micro1 = {}
        third_micro2 = {}
    """.format(top, bottom, box, variable_value, first_col_name, first_micro1, first_micro2, second_col_name,
              second_micro1, second_micro2, third_col_name, third_micro1, third_micro2))
    
        #f1-s1-t1
    v1 = df[df[first_col_name] == first_micro1][df[second_col_name] == second_micro1][df[third_col_name] == third_micro1][variable_value].values
        #f1-s1-t2
    v2 = df[df[first_col_name] == first_micro1][df[second_col_name] == second_micro1][df[third_col_name] == third_micro2][variable_value].values
        #f1-s2-t1
    v3 = df[df[first_col_name] == first_micro1][df[second_col_name] == second_micro2][df[third_col_name] == third_micro1][variable_value].values
        #f1-s2-t2
    v4 = df[df[first_col_name] == first_micro1][df[second_col_name] == second_micro2][df[third_col_name] == third_micro2][variable_value].values
    
        #f2-s1-t1
    v5 = df[df[first_col_name] == first_micro2][df[second_col_name] == second_micro1][df[third_col_name] == third_micro1][variable_value].values
        #f2-s1-t2
    v6 = df[df[first_col_name] == first_micro2][df[second_col_name] == second_micro1][df[third_col_name] == third_micro2][variable_value].values
        #f2-s2-t1
    v7 = df[df[first_col_name] == first_micro2][df[second_col_name] == second_micro2][df[third_col_name] == third_micro1][variable_value].values
        #f2-s2-t2
    v8 = df[df[first_col_name] == first_micro2][df[second_col_name] == second_micro2][df[third_col_name] == third_micro2][variable_value].values
    
    print("""
    {variable_value} value1: {v1}
    column {first_col_name} is {first_micro1}
    column {second_col_name} is {second_micro1}
    column {third_col_name} is {third_micro1}
    
    
    {variable_value} value2: {v2}
    column {first_col_name} is {first_micro1}
    column {second_col_name} is {second_micro1}
    column {third_col_name} is {third_micro2}
    
    
    {variable_value} value3: {v3}
    column {first_col_name} is {first_micro1}
    column {second_col_name} is {second_micro2}
    column {third_col_name} is {third_micro1}
    
    
    {variable_value} value4: {v4}
    column {first_col_name} is {first_micro1}
    column {second_col_name} is {second_micro2}
    column {third_col_name} is {third_micro2}
    
    
    {variable_value} value5: {v5}
    column {first_col_name} is {first_micro2}
    column {second_col_name} is {second_micro1}
    column {third_col_name} is {third_micro1}
    
    
    {variable_value} value6: {v6}
    column {first_col_name} is {first_micro2}
    column {second_col_name} is {second_micro1}
    column {third_col_name} is {third_micro2}
    
    
    {variable_value} value7: {v7}
    column {first_col_name} is {first_micro2}
    column {second_col_name} is {second_micro2}
    column {third_col_name} is {third_micro1}
    
    
    {variable_value} value8: {v8}
    column {first_col_name} is {first_micro2}
    column {second_col_name} is {second_micro2}
    column {third_col_name} is {third_micro2}
    
    """.format(first_col_name=first_col_name, second_col_name=second_col_name, third_col_name=third_col_name,v5=v5,
               first_micro1=first_micro1, first_micro2=first_micro2, second_micro1=second_micro1,v3=v3, v4=v4,
               second_micro2=second_micro2, third_micro1=third_micro1, third_micro2=third_micro2, v1=v1, v2=v2,
               v6=v6, v7=v7, v8=v8, variable_value=variable_value
              ))
    
    return [v1, v2, v3, v4, v5, v6, v7, v8]

def return_conditional_values_22(df, variables): # returning values for boxplot
    bottom = variables["names"]["bottom"]
    box = variables["names"]["box"]
    
    variable_value = variables["variables_value"]
    first_col_name = bottom
    first_micro1 = variables[first_col_name][0]
    first_micro2 = variables[first_col_name][1]
    
    second_col_name = box
    second_micro1 = variables[second_col_name][0]
    second_micro2 = variables[second_col_name][1]
    
    
    print("""
    2 by 2 plot data summary:
    
    bottom name = {}
    box name = {}
    
    variable_value = {}
    
    first_col_name = {}
        first_micro1 = {}
        first_micro2 = {}
    
    second_col_name = {}
        second_micro1 = {}
        second_micro2 = {}
    
    """.format(bottom, box, variable_value, first_col_name, first_micro1, first_micro2, second_col_name,
              second_micro1, second_micro2))
    
        #f1-s1
    v1 = df[df[first_col_name] == first_micro1][df[second_col_name] == second_micro1][variable_value].values
        #f1-s2
    v2 = df[df[first_col_name] == first_micro1][df[second_col_name] == second_micro2][variable_value].values
        #f2-s1
    v3 = df[df[first_col_name] == first_micro2][df[second_col_name] == second_micro1][variable_value].values
        #f2-s2
    v4 = df[df[first_col_name] == first_micro2][df[second_col_name] == second_micro2][variable_value].values
    
    print("""
    {variable_value} value1: {v1}
    column {first_col_name} is {first_micro1}
    column {second_col_name} is {second_micro1}
    
    
    {variable_value} value2: {v2}
    column {first_col_name} is {first_micro1}
    column {second_col_name} is {second_micro2}
    
    
    {variable_value} value3: {v3}
    column {first_col_name} is {first_micro2}
    column {second_col_name} is {second_micro1}
    
    
    {variable_value} value4: {v4}
    column {first_col_name} is {first_micro2}
    column {second_col_name} is {second_micro2}
    
    
    """.format(first_col_name=first_col_name, second_col_name=second_col_name,  v1=v1, v2=v2, v3=v3, v4=v4,
               first_micro1=first_micro1, first_micro2=first_micro2, second_micro1=second_micro1,
               second_micro2=second_micro2, variable_value=variable_value))
    
    return [v1, v2, v3, v4]


def set_names(variables, top, bottom, box):
    temp = defaultdict()
    temp["names"] = defaultdict()
    for name, subnames in variables.items():
        if top == name:
            temp["names"].update({"top" : name})
        elif bottom == name:
            temp["names"].update({"bottom" : name})
        elif box == name:
            temp["names"].update({"box" : name})
    
    temp["names"] = dict(temp["names"])
    variables.update(temp)
    
    return variables

def draw22(values, variables, notch=False, title="boxplot_result"):
    label_title = variables["names"]["bottom"]
    labels = variables[label_title]
    
    color_title = variables["names"]["box"]
    color_names = variables[color_title]
    
    value_name = variables["variables_value"]
    
    left_positions=[-0.4, 0.4]
    right_positions=[1.6, 2.4]
    ticks=[0, 2]
    
    left_color = ['pink']
    right_color = ['lightgreen']
    
    
    # first plot
    fig = plt.figure(figsize=(10, 8))
    fig.suptitle(title, fontsize=35)
    
    left_group1 = [values[0], values[1]]
    right_group1 = [values[2], values[3]]

    bplot1_1 = plt.boxplot(left_group1[0], widths=0.35,
                             positions=[left_positions[0]],
                             notch=notch,
                             patch_artist=True)  
    bplot1_2 = plt.boxplot(left_group1[1], widths=0.35,
                             positions=[left_positions[1]],
                             notch=notch,
                             patch_artist=True)  
    bplot2_1 = plt.boxplot(right_group1[0], widths=0.35,
                             positions=[right_positions[0]],
                             notch=notch,
                             patch_artist=True)  
    bplot2_2 = plt.boxplot(right_group1[1], widths=0.35,
                             positions=[right_positions[1]],
                             notch=notch,
                             patch_artist=True)  
    plt.xticks(ticks, labels, fontsize=15)
    
    for bplot in (bplot1_1, bplot1_2, bplot2_1, bplot2_2):
        if bplot == bplot1_1 or bplot == bplot2_1:
            for patch, color in zip(bplot['boxes'], left_color):
                patch.set_facecolor(color)
        else:
            for patch, color in zip(bplot['boxes'], right_color):
                patch.set_facecolor(color)

    plt.grid(True)
    plt.xlabel(label_title, fontsize=20)
    plt.ylabel(value_name, fontsize=20)
    plt.legend([bplot1_1["boxes"][0], bplot1_2["boxes"][0]], color_names, loc='upper right', fontsize=15)
    plt.savefig("./"+title+".jpg", dpi=400)
    plt.show()
    
def draw222(values, variables, notch=False, title="boxplot_result"):
    label_title = variables["names"]["bottom"]
    labels = variables[label_title]
    
    top_title = variables["names"]["top"]
    titles = variables[top_title]
    
    color_title = variables["names"]["box"]
    color_names = variables[color_title]
    
    value_name = variables["variables_value"]
    
    left_positions=[-0.4, 0.4]
    right_positions=[1.6, 2.4]
    ticks=[0, 2]
    
    left_color = ['pink']
    right_color = ['lightgreen']
    
    
    # first plot
    fig = plt.figure(figsize=(10, 8))
    fig.suptitle(titles[0], fontsize=35)
    
    left_group1 = [values[0], values[1]]
    right_group1 = [values[2], values[3]]

    bplot1_1 = plt.boxplot(left_group1[0], widths=0.35,
                             positions=[left_positions[0]],
                             notch=notch,
                             patch_artist=True)  
    bplot1_2 = plt.boxplot(left_group1[1], widths=0.35,
                             positions=[left_positions[1]],
                             notch=notch,
                             patch_artist=True)  
    bplot2_1 = plt.boxplot(right_group1[0], widths=0.35,
                             positions=[right_positions[0]],
                             notch=notch,
                             patch_artist=True)  
    bplot2_2 = plt.boxplot(right_group1[1], widths=0.35,
                             positions=[right_positions[1]],
                             notch=notch,
                             patch_artist=True)  
    plt.xticks(ticks, labels, fontsize=15)
    
    for bplot in (bplot1_1, bplot1_2, bplot2_1, bplot2_2):
        if bplot == bplot1_1 or bplot == bplot2_1:
            for patch, color in zip(bplot['boxes'], left_color):
                patch.set_facecolor(color)
        else:
            for patch, color in zip(bplot['boxes'], right_color):
                patch.set_facecolor(color)

    plt.grid(True)
    plt.xlabel(label_title, fontsize=20)
    plt.ylabel(value_name, fontsize=20)
    plt.legend([bplot1_1["boxes"][0], bplot1_2["boxes"][0]], color_names, loc='upper right', fontsize=15)
    plt.savefig("./"+title+"1.jpg", dpi=400)
    plt.show()
    
    # second plot
    fig = plt.figure(figsize=(10, 8))
    fig.suptitle(titles[1], fontsize=35)

    left_group2 = [values[4], values[5]]
    right_group2 = [values[6], values[7]]

    bplot3_1 = plt.boxplot(left_group2[0], widths=0.35,
                             positions=[left_positions[0]],
                             notch=notch,
                             patch_artist=True)  
    bplot3_2 = plt.boxplot(left_group2[1], widths=0.35,
                             positions=[left_positions[1]],
                             notch=notch,
                             patch_artist=True)  
    bplot4_1 = plt.boxplot(right_group2[0], widths=0.35,
                             positions=[right_positions[0]],
                             notch=notch,
                             patch_artist=True)  
    bplot4_2 = plt.boxplot(right_group2[1], widths=0.35,
                             positions=[right_positions[1]],
                             notch=notch,
                             patch_artist=True)
    plt.xticks(ticks, labels, fontsize=15)

    for bplot in (bplot3_1, bplot3_2, bplot4_1, bplot4_2):
        if bplot == bplot3_1 or bplot == bplot4_1:
            for patch, color in zip(bplot['boxes'], left_color):
                patch.set_facecolor(color)
        else:
            for patch, color in zip(bplot['boxes'], right_color):
                patch.set_facecolor(color)

    plt.grid(True)
    plt.xlabel(label_title, fontsize=20)
    plt.ylabel(value_name, fontsize=20)
    plt.legend([bplot4_1["boxes"][0], bplot4_2["boxes"][0]], color_names, loc='upper right', fontsize=15)
    plt.savefig("./"+title+"2.jpg", dpi=400)
    plt.show()

filepath=""
top_name=""
bottom_name=""
box_name=""
top_values=""
bottom_values=""
box_values=""
variables_value=""
notch=True
title=""
size=""

filepath, top_name, bottom_name, box_name, top_values, bottom_values, box_values, variables_value, notch, title, size = config()
df = pd.read_csv(filepath)

variables = defaultdict()
if size == "222":
    variables[top_name] = top_values
variables[bottom_name] = bottom_values
variables[box_name] = box_values
variables["variables_value"] = variables_value
variables["size"] = size
variables = dict(variables)
variables = set_names(variables, top=top_name, bottom=bottom_name, box=box_name)

values=[]
if variables["size"] == "222":
    values = return_conditional_values_222(df, variables)
elif variables["size"] == "22":
    values = return_conditional_values_22(df, variables)

if variables["size"] == "222":
    draw222(values, variables, notch=notch, title=title)
else:
    draw22(values, variables, notch=notch, title=title)