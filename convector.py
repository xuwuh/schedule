import pandas as pd
import json

def excel_to_json(excel, json_part=None):
    excel_data=pd.read_excel(excel, sheet_name=None)
    res={}
    
    for sheet_name, df in excel_data.items():
        sheet_data=[]
        columns=df.columns.tolist()

        for i, row in df.iterrows():
            row_data={}
            for col in df.columns:
                row_data[col]=row[col]
            sheet_data.append(row_data)
        res[sheet_name]=sheet_data

    if json_part:
        with open(json_part, 'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=4)
        print("json файл сохранен")
    else:
        return ("файл пустой")

if __name__=="__main__":
    input_excel="data.xlsx"
    output_json="shebule_data_conv.json"
    excel_to_json(input_excel, output_json)
