Motgranskning 063 — 2026-11-20

Källgranskning av de fem beställda filerna; inga webb-, renderings-, prestanda- eller WCAG-tester körda. Färgandelar och faktisk botåtkomst är inte verifierade. Inga webbplatsfiler ändrade.

1. **Håller:** filmen har `autoplay muted loop` utan `controls` eller egen paus (`index.html:32`, `sv/index.html:34`). Poster finns redan. Reduced motion döljer filmen (`assets/site.css:54`), men ger inte övriga besökare en paus. Rekommendationen bör omfatta all långvarig bakgrundsrörelse; detta är kodbelägg, ingen fullständig WCAG-bedömning.

2. **Håller:** doctype saknas före `<html>` (`index.html:1–3`, `sv/index.html:1–4`); kontrollen hanterar taggbalans men inte deklarationer (`.github/scripts/check_html.py:11–28,35–36`). Utan en tillagd doctype i publiceringsledet blir resultatet quirks mode. Front matter måste ligga kvar först i källfilen; doctype ska följa efter den och bli först i genererad HTML. Publicerad DOM har inte kontrollerats.

3. **Håller delvis:** `min-height:100svh` finns (`assets/site.css:29`), följt av bokningsbandet (`index.html:44`, `sv/index.html:46`); på desktop stöder det slutsatsen att bandet börjar nedanför första vyn. Procentandelarna kan inte härledas ur CSS och är inte verifierade här. Filmöverlägg (`assets/site.css:45`) gör dessutom pixelandel och upplevd färgdominans olika saker. På mobil är `svh` inte alltid hela den aktuellt synliga höjden.

4. **Håller delvis:** båda sektionerna saknar h2 (`index.html:71–96`, `sv/index.html:73–98`). Men ”h3 under h1” är missvisande: föregående h2 finns redan (`index.html:65`, `sv/index.html:67`), så en platt rubriklista kan snarare placera dem under fel avsnitt. Byt etiketterna till h2 i båda språkversionerna. `.tag` återställer inte rubrikernas typsnitt, radavstånd eller teckenavstånd (`assets/site.css:17–18,67`); samma utseende kräver uttrycklig kontroll.

5. **Håller delvis:** lokala metadata och engelsk erbjudandetext är belagda (`sv/index.html:7–8,190`). Ägarpositionen den 19 november är en uppgift i briefen, inte självständigt verifierad här. Synlig text säger redan Norden (`sv/index.html:107`), liksom engelska sidan (`index.html:37,173`); geografierna motsäger därför inte nödvändigtvis varandra. Engelsk JSON-LD-text är en lokaliseringsbrist, inte i sig ett sakfel. Samordna metadata, `#skane`-text och `areaServed` (`sv/index.html:102–108,187`), men skilj verksamhetsområde från bolagets adress (`sv/index.html:186`).

6. **Håller delvis:** `robots.txt:1–2` tillåter alla sökvägar. GitHub Pages anges i `README.md:9`, men hosting bevisar inte avsaknad av DNS-/proxyfilter eller faktisk åtkomst. Uppgiften om tidigare misslyckad livekontroll kan inte verifieras från filerna. Låt robots stå; kontrollera senare startsidor, robots och sitemap med relevanta bot-user-agenter från en anslutning som når domänen.

7. **Håller för startsidorna:** ingen Markdown-motsvarighet eller `llms.txt` hittades i filträdet; ingen sådan alternativrepresentation länkas i sidhuvudena (`index.html:8–22`, `sv/index.html:9–24`). Webbplatsen har däremot Markdown-källor för veckobreven (`README.md:24`). Avsaknaden visar inte att startsidorna är oläsbara för agenter: centralt innehåll ligger redan i HTML.

**Fråga 1 — fel och viktigare luckor:**

- **S1, rörelsereserven:** vid filmfel aktiveras oändliga SVG-animationer på 55/90 sekunder utan paus (`assets/site.css:49–54`, `index.html:32`, `sv/index.html:34`). Slå ihop detta med filmåtgärden. Att endast dölja video med CSS visar inte att hämtning/uppspelning stoppas; kontrollera reduced-motion-beteendet även på medienivå.
- **S2, fel textalternativ:** diagrammets aria-label säger att konsulterna ligger högt på första axeln och AI-labben på andra, men anger axlarna i omvänd ordning mot denna beskrivning av positionerna (`index.html:49–55`, `sv/index.html:51–57`). Koordinaterna och de synliga axeltexterna ger rätt verksamhets-/teknikrelation; korrigera textalternativets axelreferenser. Detta är viktigare än mer salmon.
- Mät LCP, överförda videobytes och textkontrast över ljusa filmrutor innan prestanda eller kontrast friskförklaras (`index.html:20,32`, `assets/site.css:31,45`). Kravet ”filmen får inte vara LCP-element” är för kategoriskt; optimera uppmätt laddning och läsbarhet, inte elementets identitet. Poster finns redan; `preload="metadata"` är inget bevis på billig autoplay.
- Agentläsbarhet: bokningsadressen finns i script men HTML-länken är mailto (`index.html:144,160–161`, `sv/index.html:157,173–174`). Dokumentera denna skillnad för läsare utan JavaScript; ändra ingen skyddad bokningsadress inom designarbetet.

**Fråga 2 — ordning, strykningar och sammanslagningar:**

Ta först paus inklusive reservanimation, rubrikstruktur och diagrammets textalternativ. Behåll doctype + kontroll som en avgränsad ändring med egen visuell jämförelse före fortsatt herojustering. Flytta synkronisering av språk/geografi före kosmetik; om briefens ägarbeslut redan är auktoriserat behövs inte samma beslut igen. Gör botkontrollen oberoende av designarbetet. Stryk extra salmon som automatisk åtgärd och skjut upp Markdown/llms.txt. Ingen ändring av pris, bokningsadress eller kontaktadress föreslås.

**Fråga 3 — lägre hero och salmon:**

En lägre hero är en rimlig hypotes för att visa nästa steg, inte en bevisad lösning på ”genererad navy”. `86svh` är bara minhöjd: text, padding och mobilens staplade innehåll kan göra heron högre (`assets/site.css:29,34–40`). Prova båda språkens första vy efter doctype, inklusive zoom och lång text. Mer salmon längre ned påverkar inte första vyn och saknar motiverat användarmål; behåll paletten tills jämförelsen visar ett behov.

**Fråga 4 — doctype och layoutskydd:**

Ja, byte från quirks till standards kan ändra layout; global `box-sizing:border-box` (`assets/site.css:10`) undanröjer inte alla skillnader. Jämför Jekyll-genererad HTML före/efter, inte råfiler med front matter och Liquid (`index.html:1–2,141`, `sv/index.html:1–3,154`). Kontrollera `document.compatMode === "CSS1Compat"` efteråt. Ta första-vy- och fullsidesskärmbilder vid 1440×900 och 390×844 efter scrollning; jämför navigation, radbrytningar, hero, bokningsband, prisblock, sidfot och horisontellt överflöde. Håll filmruta och fontladdning lika i jämförelsen. Kör HTML-kontrollen och länkkontrollen när ändringen byggs. `README.md:25–26` beskriver felaktigt startsidan som utan front matter; använd inte det som testpremiss.

— Coder (Codex) on behalf of Conny Wadbro
