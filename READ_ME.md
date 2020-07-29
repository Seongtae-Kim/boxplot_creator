# Boxplot creator 사용법

Written by Seongtae Kim, Computational Linguistics, Korea University



## 실행을 위한 필수 라이브러리

```python
import matplotlib.gridspec as gridspec
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```



## 실행

```bash
$ python boxplot_creator.py
```

위와 같은 명령으로 간단하게 실행가능합니다.



실행을 위해서는 예제로 들어간 "Reciprocals.csv"와 같은 형식으로 데이터가 삽입되어 있어야 합니다.

Boxplot은 2 by 2와 2 by 2 by 2의 데이터를 모두 플롯으로 출력합니다.

생성된 이미지는 boxplot_creator.py가 있는 위치에 저장됩니다.



초기 설정을 위해서 config.txt를 다음과 같이 설정할 수 있습니다. 아래는 config.txt의 예제

```tex
filepath = ./Reciprocals.csv
top_name = Distance
bottom_name = Plurality
box_name = masked
top_values = short long
bottom_values = singular plural
box_values = sangho selo
variables_value = surprisal
notch = False
vert = True
title = Reciprocals
size = 222
```

type과 setting 명은 "="을 기준으로 구분됩니다. type명은 reserved word 역할을 하므로 아래의 단어를 대소문자를 맞춰서 넣어주시기 바랍니다.

>  **type명:** 
>
> filepath, top_name, bottom_name, box_name, top_values, bottom_values, box_values, variables_value, notch
> vert, title, size



## filepath

filepath는 분석을 위한 자료의 파일 경로를 입력해주시면 됩니다. 반드시 csv일 필요는 없지만 pandas에서 dataframe으로 인식할 수 있는 형식이어야 합니다.

​	2 by 2의 경우 최소한 2개의 컬럼 이름과 각 컬럼 이름별 categorical value가 2개씩 총합 8개가 있어야 하며

​	2 by 2 by 2의 경우 최소한 3개의 컬림 이름과 각 컬럼 이름별 categorical value가 2개씩 총합 8개가 있어야 합니다.

사이즈에 상관 없이 수치값으로 부여된 컬럼명과 value들이 하나 필요합니다.



## top_name

- top_name은 분석을 위한 자료에 있는 컬럼 헤드명과 정확히 일치해야 합니다.
- 2 by 2의 경우에는 사이즈를 22로 설정하면 빈칸으로 남겨두어도 오류가 발생하지 않습니다.
- 출력되는 이미지에서는 가장 상단에 위치하는 텍스트가 되며 2 by 2의 경우에는 가장 상단에 연구 제목(사용자가 지정 가능)으로 표시되고 2 by 2 by 2의 경우에는 2 개의 이미지 별로 각각 top_name에 해당되는 categorical value 2개가 차례대로 표시됩니다.



## top_values

- top_name에 해당하는 두 가지 categorical value입니다.
- 2 by 2의 경우에는 사이즈를 22로 설정하면 빈칸으로 남겨두어도 오류가 발생하지 않습니다.



## bottom_name

- bottom_name은 분석을 위한 자료에 있는 컬럼 헤드명과 정확히 일치해야 합니다.
- 필수 자료이며 없을경우 오류가 발생합니다.
- 출력되는 이미지에서는 가장 하단에 표시되며 2개의 박스플롯들을 하나의 그룹으로 하여 각각의 value들이 그 category를 표시합니다.



## bottom_values

- bottom_name에 해당하는 두 가지 categorical value입니다.
- 필수 자료이며 없을경우 오류가 발생합니다.



## box_name

- box_name은 분석을 위한 자료에 있는 컬럼 헤드명과 정확히 일치해야 합니다.
- 필수 자료이며 없을경우 오류가 발생합니다.
- 출력되는 이미지에서는 따로 표시되진 않지만 해당하는 value들 2개가 오른쪽 상단에 박스에 표시됩니다.



## box_values

- box_name에 해당하는 두 가지 categorical value입니다.
- 필수 자료이며 없을경우 오류가 발생합니다.



## variables_value

- 분석을 위한 자료에 수치값을 가지고 있는 컬럼 헤드명으로 정확히 일치해야 합니다.
- 필수 자료이며 없을경우 오류가 발생합니다.
- y축 라벨로 들어갑니다.



## notch

- 박스플롯에서 notch형태의 박스를 출력할 것인지 설정합니다.
  - notch 형태의 박스를 원할 경우 True를 그렇지 않을 경우 False를 설정합니다. (대소문자 주의)
- 기본값은 False입니다.



## title

- 박스 플롯 이미지의 파일명이 됩니다.

- 2 by 2의 경우 가장 상단에 제목으로 들어가게 됩니다.

  

## size

- 실험 데이터가 2 by 2인지 2 by 2 by 2인지의 경우에 따라 나뉩니다.

  > 2 by 2의 경우
  >
  > size = 22
  >
  > 
  >
  > 2 by 2 by 2의 경우
  >
  > size = 222