# Pioneer Metal / refresh_v2

## Brief and audience

A full redesign for purchasing teams, window and door manufacturers, construction-system suppliers, and OEM partners. The primary action is to explore the actual profiles and start an inquiry. Static HTML remains compatible with GitHub Pages.

## Subject inventory

- Pioneer Metal Products Factory, with its red emblem and silver material.
- Cold-rolled steel sections for window systems and industrial infrastructure.
- Steel reinforcement for uPVC and aluminium windows and doors.
- Drywall and ceiling framing.
- Custom hot-rolling, punching, and CNC work from technical drawings.
- Production-line, roller, warehouse, and shipping photographs owned by the project.
- Folded, thin-walled cross-sections photographed in Products_03.jpg.
- 9,000+ annual tons, 280+ customers, and exports to 24+ countries: existing published figures.
- 18+ years of experience and references to activity since 2006: retained published information.
- Lijialong sealing-strip cooperation, OEM customers, and Melan Trade logistics.
- FENSTERBAU FRONTALE, Nuremberg, 24–27 March 2026; FESQUA, São Paulo, 9–12 September 2026.
- Existing reinforcement-steel PDF, phone +86 136 5671 4278, email pioneermetal@163.com, WhatsApp destination, and original map coordinates.

No city or postal address has been verified. The existing map coordinates are retained without adding a city claim.

## Argument and copy deck

Home: Pioneer Metal produces cold-rolled steel profiles → name at architectural scale, material study, and real sections. The factory makes the sections → actual factory photography and company description. Supply is established → published figures and existing cooperation relationships. Find the appropriate product → working product selector with actual photographs and original descriptions. Start an inquiry → real Contact page.

About: Manufacturing Power → original factory and roller photographs. Our Story → existing company introduction, automated production, and precision-engineering information. Production and delivery → factory, machine, and shipment photographs. Capacity → the published experience and annual-tonnage figures. Partnership → all three existing cooperation descriptions.

Products: Steel Profiles → original product categories and descriptions. Steel Reinforcement → actual profiles, use in uPVC/aluminium windows and doors, real PDF. Drywall & Ceiling → actual framing images, original description, catalogue availability stated honestly. Custom Fabrication → real section photo, hot-rolling/punching/CNC description, WhatsApp inquiry.

News: Global exhibitions → both 2026 events, exact dates, locations, photographs and their product focus. Dates are presented as records rather than future invitations.

Contact: Let's connect → existing phone/email, a genuine email-inquiry form, WhatsApp, and the original location map. The form opens the visitor's email app; it does not claim to submit to a backend.

## Direction and idea

Dealt direction: The name as a monument. Seed: 840202196. Type: Bodoni Moda / Jost. Palette: Pioneer red, silver-white, graphite. The two-ink hero blueprint is resolved to one ink in accordance with the skill's headline rule.

On this page, Pioneer's name and photographed folded steel sections become a monument followed by a sequence of material and factory views. The letterforms are treated at the scale of the steel lengths in its warehouse. This is a brand treatment rather than a claim of exclusive product geometry.

Live thing: a product selector using the three existing categories, actual product images and their real catalogue/inquiry destinations. Without JavaScript its links go to the corresponding product sections.

Redraw: list-poster-lines replaced with list-sticky-photo-active-list. The original calls for four to seven very short poster words; Pioneer has three product categories with longer names and full descriptions.

## Assets and behaviour

All pre-existing asset URLs continue to reference refs/heads/main. Local copies are used only as error fallbacks. Logo_White.png is used on dark surfaces. resources/profile-study.webp is a generated artistic studio visualization, derived from Products_03.jpg, and described as such in its alt text. It is not presented as documentary factory photography or a technical drawing. There are no new statistics, testimonials, customers, specifications, or sample product claims.

Shared header/footer and page fragments live under site/. Run python3 scripts/build_site.py to regenerate the five static root pages. CSS tokens, shared interactions, translation data, reduced motion, keyboard focus, and responsive layout are centralized.

Motion: masked name entrance; individually staggered section elements; a subtle image drift; short feedback on controls. Content is visible without script and under reduced motion.

## Baseline

The old five-page source lint reported 97 FAIL and 95 WARN. The old homepage browser inspection reported 11 FAIL and 7 WARN. Its hero fit well, but stock card grids, decorative labels, small grey text, floating navigation, and inconsistent composition capped the critique at 6.0.
