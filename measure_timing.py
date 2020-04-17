import time

def time_this(num_runs=10):
	def decorator(func):
		def timer(param):
			avg_time = 0
			for _ in range(num_runs):
			    t0 = time.time()
			    func(param)
			    t1 = time.time()
			    avg_time += (t1 - t0)
			avg_time /= num_runs
			return "при количестве итераций {0}, среднее время рассчета для последовательности Фибоначи\n до {1} сотавляет: {2} секунд".format(num_runs, func(param),avg_time)
		return timer
	return decorator

if __name__ == "__main__":
    num = input("Введите порядок (степень 10) предела \n последовательности натуральных чисел Фибоначи \n  для вычисления среднего времени\n   построения последовательности: ")
    num_runs = input("Введите количество итераций: ")
    @time_this(int(num_runs))
    def fibonachi(lim):
        if int(lim):
            fibo = [1, 2]
            fi_= 3
            sum = 2
            while fi_ <= 10**int(lim):
                fibo.append(fi_)
                if not fi_ % 2:
                    sum += fi_
                fi_ = fibo[-1] + fibo[-2]
            return(fibo[-1])
        else:
        	return("error range")

    print(fibonachi(num))