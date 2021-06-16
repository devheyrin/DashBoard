import csv

import numpy as np

from config.settings import DATA_DIRS


class MyAnalysis:
    def baby(self):
        f = open(DATA_DIRS[0]+'\\age3.csv');
        data = csv.reader(f);
        next(data);
        data = list(data);

        max = 0;
        min = 9999999;
        maxrate = 0.0;
        minrate = 0.0;
        maxloc = '';
        minloc = '';

        result = [];

        for row in data:
            rdata = np.array(row[3:9], dtype=int);
            sumdata = np.sum(rdata);
            loc = row[0].split(' ')[1];
            result.append([loc, int(sumdata)]);

        return result;

            # if sumdata > max:
            #     maxrate = sumdata / int(row[1]) * 100;
            #     max = sumdata;
            #     maxloc = row[0];
            # if sumdata < min:
            #     minrate = sumdata / int(row[1]) * 100;
            #     min = sumdata;
            #     minloc = row[0];

        # print(maxloc, max, maxrate);
        # print(minloc, min, minrate);


    def pop3year(self):
        f = open(DATA_DIRS[0]+'\\age4.csv');
        data = csv.reader(f);
        next(data);
        data = list(data);

        rate = 0;
        loc = '';
        result = [];
        for row in data:
            rdata = int(row[27]) - int(row[1])
            rate = rdata / int(row[1]);
            loc = row[0];

            result.append([loc,rate])
        print(loc, rate);
        return result;



if __name__ == '__main__':
    result = MyAnalysis().baby();
    print(result);