def val(n):
    if n == 0:
        return
    print(n)
    val(n+1)

num=-10
val(num)