# Statisk SEO-granskning av transformationbeyond.se, 25 november 2026

Webbplatskartan innehåller alla tre HTML-sidor som är avsedda för indexering. Varje adress förekommer en gång och matchar sidans canonical. De båda startsidorna pekar ömsesidigt på rätt språkversion. Första åtgärden gäller JSON-LD på startsidorna. Inför första veckobrevet behöver även brevmallens beskrivning och webbplatskartans datum ses över.

Granskningen utgår från `master` vid `28dedbf`. En jämförelse med order 961 vid `4cbbd04`, som inkluderar 956, gav samma SEO-underlag. Sajten byggdes lokalt med GitHub Pages 232, Jekyll 3.10.0 och tom `baseurl` för den egna domänen. HTML, JSON-LD, sitemap och Atom lästes ur bygget. Resultatet beskriver byggfilerna. HTTP-svar i produktion, externa bilder och sökmotorernas faktiska indexering ingick inte.

## Engelska

| Sida | Resultat i byggd HTML |
| --- | --- |
| Startsidan `/` | `lang="en"`, en H1 och titeln ”AI advisory for leadership teams — Transformation & Beyond, Sweden”. Metabeskrivningen anger målgrupp, pris och två veckors leveranstid. Open Graph har engelsk titel och beskrivning, typen `website`, en bild och egen URL. Twitter-kortet anger stor bild. [Metadata](../index.html#L4-L18) · [Huvudrubrik](../index.html#L39) |
| Gemensam felsida `/404.html` | Engelsk titel och beskrivning, svensk hjälptext märkt med `lang="sv"` och länkar till båda startsidorna. Sidan har `noindex` och saknas i webbplatskartan. [Metadata](../404.html#L2-L8) · [Språklänkar](../404.html#L29-L37) |

**Canonical, hreflang och upptäckt.** Canonical och `og:url` anger `https://transformationbeyond.se/`. Engelska sidan länkar till sig själv som `en`, till `/sv/` som `sv` och till `/` som `x-default`. Svenska sidan bekräftar samma tre adresser. Roten finns i sitemap och `robots.txt` tillåter genomsökning. [Engelska länkar](../index.html#L9-L15) · [Svenska returlänkar](../sv/index.html#L10-L16) · [Sitemap](../sitemap.xml#L5-L14) · [Robots](../robots.txt#L1-L4)

**Prioritera bolagets JSON-LD.** Blocket går att läsa som JSON. Det anger bolaget, grundaren och ett `Offer` för AI Value Review på 75 000 SEK, i linje med det synliga erbjudandet. Båda språkversionerna använder däremot `ProfessionalService`, som Schema.org har fasat ut. Bolaget saknar också gemensamt `@id` och har olika `url` på de två sidorna. Använd `Organization` med samma stabila `@id` på båda språken och behåll varje sidas canonical. Om själva rådgivningstjänsten modelleras kan `Offer.itemOffered` peka på en `Service`. [Engelsk JSON-LD](../index.html#L182-L197) · [Synligt erbjudande](../index.html#L104-L117) · [Svensk JSON-LD](../sv/index.html#L195-L211) · [Schema.org om ProfessionalService](https://schema.org/ProfessionalService)

## Svenska

| Sida eller mall | Resultat i byggd HTML |
| --- | --- |
| Startsidan `/sv/` | `lang="sv"`, en H1 och en egen titel som nämner Malmö, Lund och Skåne. Metabeskrivningen anger pris exklusive moms och två veckors leveranstid. Open Graph har svensk titel och beskrivning, `sv_SE`, typen `website`, bild och egen URL. Twitter-kortet anger stor bild. [Metadata](../sv/index.html#L5-L20) · [Huvudrubrik](../sv/index.html#L41) |
| Veckobrevsarkivet `/beyond/` | Svensk titel och beskrivning, en H1, egen canonical och samma `og:url`, `og:type=website` och länk till Atom. Den granskade revisionen har noll brev, så arkivet visar sitt tomläge och flödet har noll poster. Arkivet och breven saknar engelsk motsvarighet. [Arkiv](../beyond/index.html#L3-L14) · [Tomläge](../beyond/index.html#L17-L33) · [Metadata](../_layouts/beyond-base.html#L2-L23) |
| Brevmallen `/beyond/<år>-v<vecka>/` | I ett separat provbygge fick testbrevet en egen titel med veckonummer, en H1, datum, författarnamn, egen canonical och `og:type=article`. Mallen ger en reservbild när omslag saknas. Arkiv och brev saknar JSON-LD. `BlogPosting` är en möjlig komplettering när brev publiceras. [URL-mönster](../_config.yml#L25-L34) · [Sidhuvud](../_layouts/beyond-base.html#L5-L23) · [Brev](../_layouts/beyond-letter.html#L4-L17) |
| Prenumeration `/prenumerera/` | Mellansidan har `noindex` och saknas i sitemap. Omedelbar HTML-vidarebefordran, canonical och den klickbara reservlänken går till samma prenumerationssida på Substack. [Prenumerationsmall](../prenumerera/index.html#L2-L11) |

**Canonical, hreflang och upptäckt.** Svenska startsidans canonical och `og:url` är `https://transformationbeyond.se/sv/`. Självreferensen för `sv`, returlänken till `en` och `x-default` till engelska roten stämmer med det engelska sidhuvudet. Både `/sv/` och det enspråkiga arkivet `/beyond/` finns i sitemap. Arkivets `rel="alternate"` anger ett Atom-flöde. [Språkpar](../sv/index.html#L10-L16) · [Arkivets flödeslänk](../_layouts/beyond-base.html#L23) · [Sitemap](../sitemap.xml#L6-L17)

**Prioritera språket i JSON-LD när bolagstypen uppdateras.** Det svenska blocket är giltig JSON och har samma bolagsnamn, organisationsnummer, pris och valuta som det engelska. Däremot är `makesOffer.description` ordagrant på engelska trots att erbjudandet beskrivs på svenska på sidan. Dessutom ligger `inLanguage: "sv"` på bolaget. Återanvänd den svenska erbjudandebeskrivningen i `Offer` och ange sidans språk på en `WebPage` om den läggs till. [Svensk JSON-LD](../sv/index.html#L195-L211) · [Synligt erbjudande](../sv/index.html#L117-L130) · [Schema.org om inLanguage](https://schema.org/inLanguage)

**Inför första brevet**

1. **Ge brev utan ingress en egen beskrivning.** Importen godtar ett brev med titel, brödtext och källor men utan kursiverad ingress. Ett sådant testbrev gav `content=""` för både `description` och `og:description`. Låt importen spara en kort beskrivning från första brödtextstycket när ingress saknas. Kontrollera att båda taggarna får text i det byggda brevet. [Import](../bin/import-beyond.py#L198-L209) · [Sparade fält](../bin/import-beyond.py#L283-L293) · [Beskrivningstaggar](../_layouts/beyond-base.html#L7-L12)
2. **Använd ett verifierbart ändringsdatum i sitemap.** Mallen skriver brevets publiceringsdatum som `lastmod`. Eftersom framtidsdaterade brev publiceras direkt fick ett testbrev daterat 30 november redan i bygget den 25 november `lastmod=2026-11-30`. Även en senare sakändring behåller publiceringsdatumet. Utelämna det valfria fältet tills det går att ange datumet för senaste väsentliga ändring. [Publiceringsregel](../_config.yml#L21-L28) · [Sitemap för brev](../sitemap.xml#L15-L17)

## Kontrollunderlag

Grundbygget gav fem HTML-filer. En XML-tolk läste ut exakt `/`, `/sv/` och `/beyond/` ur sitemap, alla på HTTPS och samma värd som i `CNAME` och `robots.txt`. En HTML-tolk kontrollerade språk, metadata och canonical. Båda startsidornas JSON-LD-block lästes med `json.loads`. Provbreven byggdes i separata arbetskopior. Offertmallarna under `docs/` är undantagna från publicering. [Domän](../CNAME#L1) · [Robots](../robots.txt#L1-L4) · [Byggkonfiguration](../_config.yml#L1-L16)
