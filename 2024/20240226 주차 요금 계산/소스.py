import math
def convert_time(time):
    h, m = map(int, time.split(':'))
    return h*60+m

def solution(fees, records):
    record_in_hash = {}
    record_out_hash = {}
    time_hash = {}
    fee_hash = {}

    for record in records:
        time, number, content = record.split()
        if content == 'IN':
            record_in_hash[number] = record_in_hash[number]+[time] if record_in_hash.get(number) else [time]
        else:
            record_out_hash[number] = record_out_hash[number]+[time] if record_out_hash.get(number) else [time]

    for car, in_times in record_in_hash.items():
        out_times = record_out_hash[car] if record_out_hash.get(car) else ["23:59"]
        if len(in_times)!=len(out_times):
            out_times.append("23:59")
        for in_time, out_time in zip(in_times, out_times):
            in_time, out_time = convert_time(in_time), convert_time(out_time)
            time_hash[car] = (time_hash[car]+out_time-in_time) if time_hash.get(car) else (out_time-in_time)

    for car, time in time_hash.items():
        if time <= fees[0]:
            fee_hash[car] = fees[1]
        else:
            fee = fees[1]
            fee += math.ceil((time-fees[0])/fees[2])*fees[3]
            fee_hash[car] = fee

    answer = list(zip(*sorted(list(fee_hash.items()))))[1]
    return answer


