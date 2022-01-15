# AB Testing (AB Testi)

<p align="center">
  <img src="https://raw.githubusercontent.com/celalakcelikk/hybrid_recommender_system/main/media/rs.png" alt="rs"/>
<p>

## İş Problemi
Facebook kısa süre önce mevcut **maximum bidding** adı verilen teklif verme türüne alternatif olarak yeni bir teklif türü olan **average bidding**’i tanıttı.

Müşterilerimizden biri olan **bombabomba.com**, bu yeni özelliği test etmeye karar verdi ve averagebidding’in, maximumbidding’den daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.

## Veri Seti Hikayesi
bombabomba.com’un web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.

**Kontrol** ve **Test** grubu olmak üzere iki ayrı veri seti vardır.

## Veri Seti Değişkenleri

* **Impression:** Reklam görüntüleme sayısı 
* **Click:** Tıklama. Görüntülenen reklama tıklanma sayısını belirtir.
* **Purchase:** Satın alım. Tıklanan reklamlar sonrası satın alınan ürün sayısını belirtir.
* **Earning:** Kazanç. Satın alınan ürünler sonrası elde edilen kazanç.

