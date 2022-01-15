import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel("datasets/ab_testing.xlsx", sheet_name='Control Group')
df_test = pd.read_excel("datasets/ab_testing.xlsx", sheet_name='Test Group')

####################
# Veri Analizi
####################


def check_df(dataframe, head=5, tail=5):
    print("##################### Shape #####################")
    print(dataframe.shape)

    print("##################### Types #####################")
    print(dataframe.dtypes)

    print("##################### Head #####################")
    print(dataframe.head(head))

    print("##################### Tail #####################")
    print(dataframe.tail(tail))

    print("##################### NA #####################")
    print(dataframe.isnull().sum())

    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

    print("##################### Describe #####################")
    print(dataframe.describe([0.10, 0.25, 0.50, 0.70, 0.80, 0.90, 0.95, 0.99]).T)

    print("##################### Info #####################")
    print(dataframe.info())


check_df(df_control)
check_df(df_test)

############################
# İki grubun Purchaselerinin ortalaması arasında anlamlı bir fark yok mudur?
############################

############################
# Normallik Varsayımı
############################

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.


def varyans_control(df_cloumn, p_value=0.05):
    test_stat, pvalue = shapiro(df_cloumn)
    print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
    if pvalue < p_value:
        print("H0 red edilir.")
    else:
        print("H0 reddedilemez.")


varyans_control(df_cloumn=df_control["Purchase"])
varyans_control(df_cloumn=df_test["Purchase"])


############################
# Varyans Homojenligi Varsayımı‚
############################

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

def homojen_control(df_cloumn1, df_cloumn2, p_value=0.05):
    test_stat, pvalue = levene(df_cloumn1,
                               df_cloumn2)
    print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
    if pvalue < p_value:
        print("H0 red edilir.")
    else:
        print("H0 reddedilemez.")
    

homojen_control(df_cloumn1=df_control["Purchase"], df_cloumn2=df_test["Purchase"])

############################
# Hipotezin Uygulanması
############################

# 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
# 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)

# Eğer normallik sağlanmazsa her türlü nonparametrik test yapacağız.
# Eger normallik sağlanır varyans homojenliği sağlanmazsa ne olacak?
# T test fonksiyonuna arguman gireceğiz.


# H0: M1 = M2 (... iki grup ortalamaları arasında ist ol.anl.fark yoktur.)
# H1: M1 != M2 (...vardır)

############################
# Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
############################

def ttest_control(df_cloumn1, df_cloumn2, p_value=0.05):
    test_stat, pvalue = ttest_ind(df_cloumn1,
                              df_cloumn2,
                              equal_var=True)
    print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
    if pvalue < p_value:
        print("H0 red edilir.")
    else:
        print("H0 reddedilemez.")


ttest_control(df_cloumn1=df_control["Purchase"], df_cloumn2=df_test["Purchase"])

############################
# Hangi testi kullandınız? Neden?
############################

"""
İlk adım olarak iki grubun normallik dağılımlarını kontrol edildi. 
Kontrol sonucu ik grubunda dağılımının normallik dağılım için uygun olduğu sonucuna varıldı.
Bu yüzden grubların homojenlik durumlarının kontrol edilmesine karar verildi.
Homojenlik durum kontrol sonucunda dağılım homojen olduğu kanısına varıldı.
Kontroller sonucu, "Bağımsız İki Örneklem T Testi" uygulanmasının uygun olacağına karar verildi.
Uygulama sonucu  p-value > 0.05 olduğu için H0 hipotezi reddedilemeyeceğini sonucuna varıldı.
"""

############################
# Soru 2'ye verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir ? Satın alma anlamında anlamlı bir fark
############################

"""
Satın alma üzerinden bakıldığında gruplar arasında anlamlı bir fark olmadığı gözlemlenmiştir. 
Önerilen yöntemler;
1. İki yöntemden biri seçilebilir.
2. Tıklama, Etkileşim vs. farklılıklarda incelenebilir.
3. Var olan yöntemle de devam edilebilir.
"""
