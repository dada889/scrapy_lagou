import pandas as pd


def derive_table(tbody_soup):
    tbody_list = []
    trs = tbody_soup.select('tr')
    for tr in trs:
        rows = tr.select('td')
        list_rows = [row.text.strip() for row in rows]
        if list_rows:
            tbody_list.append(list_rows)
    df = pd.DataFrame(tbody_list)
    filter_col = (df == '').apply(lambda x: not all(x), axis=0)
    return df.ix[:, filter_col]