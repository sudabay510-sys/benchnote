from helpers import L, LM, opt, env_names

Q = [
    {"id": "craft", "type": "choice", "prompt": "What do you make?",
     "options": [opt("jewelry", "Jewelry"), opt("ceramics", "Ceramics / pottery"), opt("textile", "Sewing / knit / textile"), opt("paper", "Paper goods / prints"), opt("candles", "Candles / bath"), opt("wood", "Wood / home goods")]},
    {"id": "stage", "type": "choice", "prompt": "Where is your shop right now?",
     "options": [opt("idea", "Not open yet"), opt("new", "Open, under 20 listings"), opt("steady", "20–100 listings"), opt("big", "100+ listings")]},
    {"id": "markets", "type": "choice", "multi": True, "prompt": "Where do you sell (or plan to)?", "help": "Select all that apply.",
     "options": [opt("etsy", "Etsy"), opt("site", "Own website"), opt("fairs", "Craft fairs / markets"), opt("wholesale", "Local shops / wholesale"), opt("social", "Instagram / TikTok")]},
    {"id": "make_time", "type": "choice", "prompt": "Hours per week for making?",
     "options": [opt("5", "Under 5"), opt("10", "5–15"), opt("20", "15–30"), opt("30", "30+")]},
    {"id": "photos", "type": "choice", "prompt": "How do you feel about your product photos?",
     "options": [opt("good", "Happy with them"), opt("ok", "They’re okay"), opt("bad", "They hold me back")]},
    {"id": "pricing", "type": "choice", "prompt": "How do you set prices today?",
     "options": [opt("formula", "A formula with materials + time"), opt("compare", "I look at similar shops"), opt("guess", "Honestly, I guess"), opt("unsure", "Not priced yet")]},
    {"id": "struggle", "type": "choice", "prompt": "What’s the hardest part right now?",
     "options": [opt("consistency", "Listing consistently"), opt("titles", "Titles, tags & descriptions"), opt("launch", "Planning a launch / collection"), opt("time", "Balancing making vs. selling")]},
    {"id": "season", "type": "choice", "prompt": "What’s your next big selling moment?",
     "options": [opt("holiday", "Winter holidays"), opt("valentine", "Valentine’s / spring"), opt("wedding", "Wedding season"), opt("none", "No specific season")]},
]


def plan(a):
    craft = L(Q[0]["options"], a.get("craft"))
    t = {"5": 2, "10": 3, "20": 5, "30": 7}.get(a.get("make_time"), 3)
    struggle = a.get("struggle", "consistency")
    focus = {
        "consistency": "Batch 3 listings every week on the same day — draft, photograph, publish.",
        "titles": "Rewrite your top 5 titles: what it is, material, size/color, who it’s for — plain language first.",
        "launch": "Pick one 6–8 piece mini collection and work back from a launch date 4 weeks out.",
        "time": "Split your week: make days and one 90-minute ‘shop desk’ block.",
    }[struggle]
    return {
        "title": f"Benchnote 30-day cadence — {craft}",
        "summary": f"Built around ~{t} new or refreshed listings per week, sold through {LM(Q[2]['options'], a.get('markets') or ['etsy'])}. Main focus: {L(Q[6]['options'], struggle).lower()}. Benchnote is a planning tool — we never promise sales or income.",
        "preview_sections": [
            {"title": "This week’s focus (unlocked)", "bullets": [focus, "Photograph in daylight next to a window; same backdrop for a consistent shop look.", "Write one listing description template you can reuse."]},
            {"title": "Pricing check", "body": "Add up materials, packaging, fees, and an hourly rate for your time. Compare that floor with similar shops before you decide. This is a worksheet, not financial advice."},
            {"title": "Weekly rhythm", "bullets": ["Mon: make", "Tue: make", "Wed: photos + listings", "Thu: make", "Fri: one social post + answer messages"]},
        ],
        "locked_sections": [
            {"title": "Day-by-day 30-day calendar", "teaser": "Listing, photo, and post tasks for every day."},
            {"title": "Title & tag checklist", "teaser": "A plain-language checklist for searchable listings (education only)."},
            {"title": "Mini-collection launch timeline", "teaser": "4-week countdown without fake urgency."},
            {"title": "Seasonal packs", "teaser": "Holiday, wedding, and spring prep." },
        ],
    }


BRAND = {
    "name": "Benchnote", "slug": "benchnote", "port": 5109,
    "tagline": "A listing, photo, and launch cadence for handmade sellers.",
    "eyebrow": "For makers & handmade shops",
    "hero_title": "Make more. Panic-list less.",
    "hero_lede": "Benchnote asks about your craft, making time, and where you sell, then builds a 30-day rhythm for listings, photos, and a calm collection launch.",
    "cta_primary": "Build my shop rhythm", "cta_short": "Start quiz",
    "cta_band_title": "Your work deserves a steady shop.",
    "cta_band_text": "A cadence that protects making time and keeps listings fresh.",
    "honesty_line": "Planning help only. No sales, ranking, or income promises.",
    "audience_line": "Side-hustle and full-time makers selling on Etsy, their own site, or at markets.",
    "personas": [
        {"title": "New maker", "text": "Ready to open, not sure what to list first."},
        {"title": "Weekend seller", "text": "A day job and a shop that goes quiet for weeks."},
        {"title": "Full-time maker", "text": "Busy making, behind on listings and launches."},
    ],
    "journey": [
        {"stage": "Make", "pain": "Selling tasks eat making time.", "fix": "Make days plus one shop-desk block."},
        {"stage": "Photograph", "pain": "Photos look different every time.", "fix": "One window, one backdrop, one checklist."},
        {"stage": "List", "pain": "Listings go up in random bursts.", "fix": "A weekly batch day and reusable templates."},
        {"stage": "Launch", "pain": "Collections drop with no plan.", "fix": "A 4-week countdown — no fake scarcity."},
    ],
    "how_steps": [
        {"title": "Quiz your shop", "text": "Craft, stage, channels, time, and struggles."},
        {"title": "Preview your rhythm", "text": "This week’s focus plus your weekly routine."},
        {"title": "Join the founding list", "text": "No charge today — we’ll email when checkout opens."},
    ],
    "features": [
        {"title": "30-day calendar", "text": "Listings, photos, and posts mapped to your hours."},
        {"title": "Pricing worksheet", "text": "Materials + fees + your time, written down."},
        {"title": "Launch timeline", "text": "Collections without countdown-timer tricks."},
        {"title": "Seasonal packs", "text": "Subscription: holiday and wedding-season prep."},
    ],
    "sample_peek": ["Wednesday listing batch", "Window-light photo setup", "Pricing floor worksheet", "4-week mini-collection launch"],
    "trust_points": [
        {"title": "Not affiliated with Etsy", "text": "Follow each marketplace’s own seller rules."},
        {"title": "No earnings claims", "text": "We never show income screenshots or promises."},
        {"title": "Honest launches", "text": "No fake ‘only 2 left’ tactics."},
    ],
    "faq": [
        {"q": "Will Benchnote get me more Etsy sales?", "a": "We don’t promise sales or rankings. It gives you a steady plan for the work you control."},
        {"q": "Is this SEO software?", "a": "No. It includes an educational title-and-tag checklist, not keyword tools."},
        {"q": "I sell at markets, not online. Does it fit?", "a": "Yes — choose craft fairs in the quiz and the plan adjusts."},
    ],
    "pricing": [
        {"id": "4w", "name": "4-week rhythm", "intro": "$15", "period": "first 4 weeks", "renewal": "$19 / 4 weeks", "includes": ["30-day calendar", "Pricing worksheet", "Listing templates"]},
        {"id": "12w", "name": "12-week season", "intro": "$39", "period": "first 12 weeks", "renewal": "$49 / 12 weeks", "featured": True, "includes": ["Everything in 4-week", "Launch timeline", "Seasonal packs"]},
    ],
    "disclaimer_short": "Planning education only. Not affiliated with Etsy. No sales, ranking, or income guarantees.",
    "disclaimer_long": "Benchnote provides general planning and education for handmade sellers. It is not affiliated with Etsy or any marketplace, does not guarantee sales, search ranking, or income, and is not financial or tax advice. Follow each marketplace’s seller policies. No payments are processed on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Young+Serif&family=Figtree:wght@400;500;700&display=swap",
    "fonts": ("Young Serif", "Figtree"),
    "questions": Q, "generate_plan": plan,
    "voice": "Encouraging studio-mate. Hands-on, a little craft-y, never salesy.",
    "palette": {"Background (linen)": "#FBF6F1", "Alt": "#F3E9E0", "Card": "#FFFFFF", "Ink": "#2E2230", "Muted": "#6C5D6E", "Accent (plum)": "#7B3F6E", "Accent hover": "#62305A", "Highlight (marigold)": "#E9A23B"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="20" fill="#7B3F6E"/><path d="M14 40h36" stroke="#FBF6F1" stroke-width="4" stroke-linecap="round"/><path d="M20 40v8M44 40v8" stroke="#FBF6F1" stroke-width="4" stroke-linecap="round"/><path d="M26 40c0-8 2-14 6-18 4 4 6 10 6 18" fill="#E9A23B"/></svg>',
    "css_vars": """
  --bg:#FBF6F1;--bg-alt:#F3E9E0;--card:#FFFFFF;--ink:#2E2230;--muted:#6C5D6E;--line:#E7D9CD;
  --accent:#7B3F6E;--accent-2:#62305A;--on-accent:#FFF8FB;--hi:#E9A23B;--radius:22px;
  --font-display:'Young Serif', Georgia, serif;--font-body:'Figtree', system-ui, sans-serif;
  --shadow-card:0 18px 40px rgba(123,63,110,.10);--shadow-btn:0 8px 20px rgba(123,63,110,.25);
  --cta-band-bg:#7B3F6E;--cta-band-ink:#FBF6F1;--cta-band-btn:#E9A23B;--cta-band-btn-ink:#2E2230;--tracking:-0.01em;
""",
    "personality": "background:radial-gradient(600px 320px at 90% 10%, #F6D9A8 0%, transparent 60%), radial-gradient(700px 360px at 0% 100%, #EBD3E4 0%, transparent 60%), var(--bg);",
    "extra_css": ".btn{border-radius:999px}.dot{background:var(--hi)}",
    "dos": ["Celebrate the craft; respect making time.", "Show the pricing worksheet as a tool, not advice."],
    "donts": ["Show income screenshots or earnings claims (FTC).", "Use fake scarcity in launch copy."],
}
BRAND.update(env_names("benchnote"))
