def calculator_1(age:int, hight:int, wight:int, life_style, gender:str) -> int:

    '''калькулятор,который считает суммарную норму калорий для поддержания веса'''

    k = {'very_low':1.2 , 'low':1.375, 'middle':1.55, 'hard':1.725}

    if gender == "man":
        norm_calories_1 = round(k[life_style]*(10*int(wight) + 6.25*int(hight) - 5*int(age) + 5))
    elif gender == "woman":
        norm_calories_1 = round(k[life_style]*(10*int(wight) + 6.25*int(hight) - 5*int(age) - 161))
    return norm_calories_1


    #Для поддержания формы нужно есть: 0.3 белка, 0.3 жира, 0.4 углеводов.
    #Для похудения нужно есть: 0.4 белка, 0.15 жира, 0.45 углеводов.
    #Для набора массы нужно есть: 0.35 белка, 0.15 жира, 0.5 углеводов.
    # 1 грамм жира = 9 ккал
    # 1 грамм белка = 4 ккал
    # 1 грамм углеводов = 4 ккал


def calculate_macros(age:int, hight:int, wight:int, life_style: str,gender:str, goal: str) -> list[str]:

    '''В зависимости от желания пользователя набрать,сбросить или остаться в балансе, 
    функция считает его суммарную норму калорий для этого, 
    затем отдельно рассчитывает сколько граммов белков,жиров и углеводов ему при этом нужно есть.'''

    norm_calories_1 = calculator_1(age,hight,wight,life_style,gender)
    if goal == 'gain':
        if gender == 'man':
            calories_2 = norm_calories_1 + 400
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.2 / 9
            carb = calories_2 *0.5 / 4
        elif gender == 'woman':
            calories_2 = norm_calories_1 + 250
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.2 / 9
            carb = calories_2 *0.5 / 4
    elif goal == 'loss':
        if gender == 'man':
            calories_2 = norm_calories_1 - 400
            protein = calories_2 * 0.5 / 4
            fat = calories_2 * 0.15 / 9
            carb = calories_2 *0.35 / 4
        elif gender == 'woman':
            calories_2 = norm_calories_1 - 250
            protein = calories_2 * 0.5 / 4
            fat = calories_2 * 0.15 / 9
            carb = calories_2 *0.35 / 4           
    elif goal == 'balance':
        if gender == 'man':
            calories_2 = norm_calories_1
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.3 / 9
            carb = calories_2 * 0.4 / 4
        elif gender == 'woman':
            calories_2 = norm_calories_1
            protein = calories_2 * 0.3 / 4
            fat = calories_2 * 0.3 / 9
            carb = calories_2 * 0.4 / 4
    return [round(protein), round(fat), round(carb), round(calories_2)]



def consumed_now(pr_prot: int, pr_fat: int, pr_carb: int, pr_cal: int, pr_wight: int) -> list[int]:

    #  Калорийность вводится на 100 грамм продукта 

    sum_cal = (int(pr_cal) * int(pr_wight)) / 100                  
    sum_prot = (int(pr_prot) * int(pr_wight)) / 100
    sum_fat = (int(pr_fat) * int(pr_wight)) / 100
    sum_carb = (int(pr_carb) * int(pr_wight)) / 100

    return [round(sum_prot), round(sum_fat), round(sum_carb), round(sum_cal)]



def difference(vals_r , vals_f):
    w = {'+': 'больше на', '-': 'ниже на', '0' : 'столько же,сколько ожидалось'}
    dif = list()
    for i in range(0,4):
      pred_res = vals_f[i]-vals_r[i]
      dop = list()
      if pred_res > 0:
        a = '+'
        dop.append(w[a]) 
        dop.append(pred_res)
      elif pred_res < 0:
        b = '-'
        dop.append(w[b])
        dop.append(abs(pred_res))
      elif pred_res == 0:
        c ='0'
        dop.append(w[c])
        dop.append(pred_res)
      dif.append(dop)
    return dif