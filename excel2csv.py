import re
from datetime import datetime as dt
import pandas as pd
import mojimoji


def main():
    with open(f"all.csv", "w") as fo:
        fo.write("date,西湖,河口湖,山中湖,精進湖,本栖湖\n")
        for heisei in range(10, 31+1):
            convert(fo, heisei)


def convert(fo, heisei):
    if heisei == 31:
        ext = "xlsx"
    else:
        ext = "xls"
    sheets = pd.read_excel(f"xls/{heisei}.{ext}", sheet_name=None)

    for sheet_name, df in sheets.items():
        m = re.search(r"\d+", sheet_name)
        if m is None:
            continue
        # pylint: disable=c-extension-no-member
        month = mojimoji.zen_to_han(m.group())
        if int(month) >= 4:
            year = heisei + 1988
        else:
            year = heisei + 1988 + 1
        for row in df.itertuples():
            if row[2] != "日":
                continue
            day = row[1]
            ymd = f"{year}-{month}-{day}"
            try:
                t = dt.strptime(ymd, "%Y-%m-%d")
            except ValueError as e:
                print(e)
                continue
            fo.write(t.strftime("%Y-%m-%d,"))
            fo.write(','.join(map(str, row[3:8])))
            fo.write("\n")


if __name__ == "__main__":
    main()
