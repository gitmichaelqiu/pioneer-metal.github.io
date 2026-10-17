# Exhibition announcements

`site/events.json` is the source for the News entry, dedicated event page and shared banner. Run `python3 scripts/build_site.py` after adding or editing an event. Commit the generated HTML, `events.js` and `translations.js` along with the source changes.

## Automatic status

- `startsAt` and `endsAt` are ISO timestamps with an explicit UTC offset.
- `timeZone` controls how the date is displayed; Eurasia uses `Europe/Istanbul`.
- The banner appears `bannerDays` days before the start (60 by default), says **Upcoming** before the opening, and **Live** from opening until closing.
- At closing it disappears. The News entry and details page remain, labelled **Past event**. The meeting action becomes a general team enquiry.
- Status updates at date boundaries, every 30 seconds while the page remains open, and when a tab becomes visible again. No rebuild or deployment is needed for status changes.
- Live events take priority. Otherwise, the nearest qualifying upcoming event is shown. The banner does not repeat an event on its own details page.
- This is browser-side date logic and follows the visitor device's clock. With JavaScript disabled, dated event content stays readable and the automatic banner stays hidden rather than showing a stale status.

For the 2026 fair, the organizer lists November 21–23 visiting hours as 10:00–18:00, and November 24 as 10:00–17:00, Istanbul time. The banner's Live state means the fair is in progress across those dates, not that the venue is open overnight. The configured period is November 21 at 10:00 through November 24 at 17:00 (+03:00).
Source: https://www.eurasiawindowdoorfair.com/

## Adding an event

Copy the existing entry and change the id, name, dates, time zone, venue, city, official URL and assets. Keep ids unique and URL-safe. Supply a `summaryKey` and corresponding translations in every locale in `site/strings.json`.

The reusable story and detail renderers live in `scripts/event_pages.py`. Each detail page uses the supplied partner and poster. When adding another event, provide its own partner object and translated `detailHeadingKey`, `partnerSummaryKey` and `posterIntroKey` rather than reusing the Istanbul announcement text. The banner, News story and details page need no template changes for another event with this same structure. The builder checks unique URL-safe ids, explicit time offsets and valid date ranges.

The supplied artwork is the immediate local cover. The official organizer image replaces it after it loads, with source credit; a CDN failure leaves the local artwork visible. Poster and Tonish logo provenance is in `resources/events/README.md`.
