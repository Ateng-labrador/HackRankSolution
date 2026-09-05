class FastAlgoExpoentions:
    def recursive(self, x, n):
        if n < 0:
            return self.recursive(1 / x, -n)
        elif n == 0:
            return 1
        elif n % 2 == 0:
            return self.recursive(x * x, n // 2)
        else:
            return self.recursive(x * x, (n - 1) // 2)

mesin_hitung = FastAlgoExpoentions()
print(mesin_hitung.recursive(2, 2))
