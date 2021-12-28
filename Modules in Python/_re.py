# RE(REGULAR EXPRESSION) MODULE

import re

str_ = "Python Course in 40 hour by Sadik Turan"

# re.findall
result = re.findall("Python", str_)
result = len(result)

# re.split
result = re.split(" ", str_)

# re.sub
result = re.sub(" ", "-", str_)     # or \s ==> space

# re.search
result = re.search("Python", str_)    # It gives match object
# result = result.span()              # It gives where is it
# result = result.start()
# result = result.end()
# result = result.group()             # It gives object that finded

# print(result)

"""

    [] - Köşeli parantezler arasına yazılan tüm ifadeler aranır.

        [abc]  => a         = 1 eşleşme
                  bc        = İki eşleşme
                  Python    = Eşleşme yok
        
        [a-e]  => [abcde]
        [1-5]  => [12345]
        [1-39] => [1239]

        [^abc] => a, b, c dışındaki karakterler
        [^0-9] => sayı olmayan karakterler

"""

result = re.findall("[abc]", str_)
result = re.findall("[hour]", str_)
result = re.findall("[a-h]", str_)

"""

    . - Herhangi bir karakteri temsil eder.

        .. => a     : Eşleşme yok
              bc    : 1 eşleşme
              def   : 1 eşleşme
              xyzq  : 2 eşleşme

"""

result = re.findall("...", str_)
result = re.findall("Py..on", str_)

"""

    ^ - Belirtilen string karakterle başlıyor mu ?

        ^a => a   : 1 eşleşme
              ab  : 1 eşleşme
              bac : Eşleşme yok

"""

result = re.findall("^P", str_)

"""

    $ - Belirtilen string karakterle bitiyor mu ?

        a$ => a   : 1 eşleşme
              ba  : 1 eşleşme
              bac : Eşleşme yok

"""

result = re.findall("P$", str_)

"""

    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.

        ma*n => mn   : 1 eşleşme
                man  : 1 eşleşme
                maan : 1 eşleşme
                main : Eşleşme yok (a'nın arkasından n gelmiyor.)

"""

"""

    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.

        ma+n => mn   : 1 eşleşme yok
                man  : 1 eşleşme
                maan : 1 eşleşme
                main : Eşleşme yok (a'nın arkasından n gelmiyor.)

"""

"""

    ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.

        ma?n => mn   : 1 eşleşme yok
                man  : 1 eşleşme
                maan : 1 eşleşme
                main : Eşleşme yok (a'nın arkasından n gelmiyor.)

"""

"""

    {} - Karakter sayısını kontrol eder.

        al{2}      => a karakterinin arkasına l karakteri iki kez tekrarlamalı
        al{2, 3}   => a karakterinin arkasına l karakter en az iki, en fazla üç kez tekrarlamalı
        [0-9]{24} => en az iki, en çok 4 karakterli sayılar

"""

result = re.findall("a{2}", str_)
result = re.findall("[0-9]{2}", str_)

"""

    | - Alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da be

            cde    : Eşleşme yok
            ade    : 1 eşleşme
            acdbea : 3 eşleşme

"""

"""

    () - Gruplama yapmak için kullanılır.

        (a|b|c)xy => a, b, c kaakterlerinin ardından xy gelmelidir.

"""

print(result)