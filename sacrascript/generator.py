"""Deterministic starter templates; not a historical source corpus."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Draft:
    title: str
    body: str


_LATIN = {
    "prayer": ("Oratio pro {occasion}", "Domine Iesu Christe, lux mundi et spes fidelium, respice propitius ad nos in hac hora. Da nobis cor humile, pacem in opere, misericordiam in iudicio, atque perseverantiam in bono. Per gratiam tuam dirige gressus nostros, ut proximum diligamus et nomen tuum reverenter benedicamus. Amen."),
    "blessing": ("Benedictio pro {occasion}", "Benedicat nos Deus omnipotens, Pater et Filius et Spiritus Sanctus. Confortet corda nostra, custodiat domos nostras, et doceat nos in pace atque caritate ambulare. Amen."),
    "sermon": ("Admonitio de {occasion}", "Fratres carissimi, fides non solum verbis, sed operibus ostenditur. Misericordia cor hominis aperit; humilitas superbiam temperat; pax autem communitatem aedificat. Consideremus igitur opera nostra et quaeramus bonum proximi, memorantes nos omnes gratia Dei indigere."),
    "blog": ("De {occasion}", "Communitas nostra hac occasione ad orationem, caritatem et mutuum auxilium invitatur. Traditio christiana nos admonet ut fidem non solum celebremus, sed etiam in cotidiana vita exerceamus."),
}
_POLISH = {
    "prayer": ("Modlitwa: {occasion}", "Panie Jezu Chryste, Światłości świata i nadziejo wiernych, spójrz łaskawie na nas w tej chwili. Daj nam pokorne serce, pokój w działaniu, miłosierdzie w osądzie i wytrwałość w dobru. Prowadź nasze kroki, abyśmy kochali bliźniego i z szacunkiem błogosławili Twoje imię. Amen."),
    "blessing": ("Błogosławieństwo: {occasion}", "Niech Bóg wszechmogący umocni nasze serca, strzeże naszych domów i uczy nas kroczyć drogą pokoju oraz miłości. Niech udzieli nam roztropności w słowach, dobroci w czynach i gotowości do pomocy bliźnim. Amen."),
    "sermon": ("Rozważanie: {occasion}", "Najmilsi, wiara objawia się nie tylko w słowach, lecz także w czynach. Miłosierdzie otwiera ludzkie serce, pokora poskramia pychę, a pokój buduje wspólnotę. Przyjrzyjmy się własnemu postępowaniu i szukajmy dobra bliźniego, pamiętając, że wszyscy potrzebujemy Bożej łaski."),
    "blog": ("Wspólnota i {occasion}", "Z tej okazji nasza wspólnota jest zaproszona do modlitwy, miłości bliźniego i wzajemnej pomocy. Chrześcijańska tradycja przypomina, że wiary nie tylko się naucza i celebruje, lecz także wprowadza w codzienne życie. Niech ten dzień stanie się okazją do pojednania i konkretnego dobra."),
}


def _format(template, occasion):
    title, body = template
    readable = occasion.strip().replace("-", " ")
    return Draft(title.format(occasion=readable), body)


def generate(kind, occasion, language="polish", audience="parish", title=None):
    """Generate a simple draft. Audience is reserved for richer future templates."""
    del audience
    if kind not in _LATIN:
        raise ValueError(f"Unsupported kind: {kind}")
    if language not in {"latin", "polish", "bilingual"}:
        raise ValueError(f"Unsupported language: {language}")
    if not occasion or not occasion.strip():
        raise ValueError("Occasion must not be empty.")
    latin = _format(_LATIN[kind], occasion)
    polish = _format(_POLISH[kind], occasion)
    sections = [title.strip()] if title else []
    if language in {"latin", "bilingual"}:
        sections.extend([latin.title, latin.body])
    if language == "bilingual":
        sections.append("")
    if language in {"polish", "bilingual"}:
        sections.extend([polish.title, polish.body])
    return "\n".join(sections)
