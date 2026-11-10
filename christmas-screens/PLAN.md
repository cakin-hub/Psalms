# God With Us: 3-wall screen rework (S5 art plan)

Nov 10, 2026. This combines three adviser reviews (stage layout, kids' text, picture-book art direction) and Chase's notes. Chase's verdict was: only screen 3 works; the rest have weird cuts; the text bubble and the split panels aren't working.

## What was wrong

- **Weird cuts:** one wide painting was sliced across the walls, so the black gaps cut through people (screens 1, 7). The gaps also cut Joseph, Leo and the sheep in half on 2, 4, 5 and 9.
- **Blur:** five screens had side walls that were just a blurred stretch of the center picture (2, 4, 5, 9, 10).
- **Splits:** two different book panels were glued into one center image (6, 8, 10). There were also seams on 1, 4, 5 and 9.
- **White paper:** the cloud, torn-paper and smoke edges on white show up as glaring white light in a dark room.
- **Text bubble:**
  - The navy box moved around: top, bottom, then both on one screen.
  - It changed size.
  - It was doubled on both side walls, while the kids face the center.
  - It projects as a dull grey hole and covered art.
  - It was always on, so it never worked as a "your turn!" signal.

## Why screen 3 works, and the rule for every screen

Each wall is its own complete, full-bleed painting of the same place in the same light.

| Wall | Size | What goes there |
|---|---|---|
| **Left** | 864×1152 (3:4 portrait) | Scenery from the same place, looking back. No main characters; at most one small animal as a find-it treat. |
| **Center** | 1440×1152 (5:4) | The story moment. All main characters, faces toward the audience. This is also the picture-book page. |
| **Right** | 864×1152 (3:4 portrait) | Scenery from the same place, looking ahead to the next beat. Same rules as the left wall. |

- **Make each wall as its own image. Never slice a panorama.** Generate at about 2× and scale down.
- **Nothing crosses the gaps.** Keep heads and hands inside the central 85% of every wall.
- **Floor or horizon line:** about 65% down on all three walls (y ≈ 750).
- **Lighting:** one light source per screen (lantern, angel or star), placed in the center. The side walls are about one stop darker and get darker toward their outer edges.
- **Edges:** full-bleed everywhere. No white paper, torn, cloud or smoke edges.
- **Pine cone:** it appears only on the center wall. The Spanish no-pine-cone edition swaps only the center image (`NN-C-sin`), and the side walls are shared.

## Kids' answer text (built by `build_screens.py`)

- **Where:** center wall only, in the top band. No more side-wall bubbles.
- **When:** two frames per screen.
  - **NNa** is art only. **NNb** adds the answer, and the operator clicks to it on the cue.
  - **Screen 4** gets three frames (4b/4c/4d), so "No room!" grows as the kids get louder.
  - **Screens 2 and 8** have no answer, so they get one frame each.
- **Look:**
  - Font: **Fredoka** SemiBold, about 132px (8% of wall height). No box.
  - Warm fill with a dark rounded outline and a soft glow.
  - The theme line "God will be with us!" is always **gold**, so pre-readers learn that the gold words mean the phrase. Other answers are cream.
  - On pale art, the colors switch automatically to dark brown ink.
- **Whisper (screen 6):** smaller, pale and outline-free: "God will be with us…"
- **Soft final line (screen 10):** candle gold with a halo. Leave it up through the candle moment.
- **Spanish:** fits on one line automatically, about 107px for «¡Dios estará con nosotros!». The « » marks are not shown on screen.
  - Screen 7 uses **¡Bebé!**, per Chase's note in S4.
- **Screen 3** keeps its current art, so its text sits upper-left over the open wall, away from Gabriel's head.

## Art prompts

### Production rules
1. **References:** upload the **original Leo & Grandpa character sheet** and **screen 3's center (Gabriel and Mary)** with every job. Once one Leo comes out right, add him as a third reference for every Leo shot.
2. **Order:** generate each screen's **center first**, then use it as the palette reference for its two side walls.
3. **Output:** name files `NN-L.png`, `NN-C.png`, `NN-R.png` (plus `NN-C-sin.png`) and put them in one folder. `build_screens.py` does the rest.

### Style guide (put this before every prompt)
> Warm hand-painted children's picture-book illustration in gouache and watercolor on cream cold-press paper. You can see the paper grain and soft wet-edge pooling. Loose, confident sepia-brown ink outlines that vary in weight. Palette: honey gold, ochre, warm sand, soft terracotta and dusty blue, with deep blue-grey for night. Light is glowing and golden, like lamplight or candlelight, with soft blooms and no harsh shadows. Simple, gentle faces: small dark oval eyes, a short curved nose line, rosy cheeks, calm kind expressions. A few large, clearly drawn figures in a simple setting with plenty of breathing room. Painted all the way to every edge of the frame. Cozy, reverent, tender. Single complete scene, no text.

### Character descriptions (copy word for word)
- **Leo:** a small 6-year-old boy who matches the character sheet reference exactly. He has short dark curly hair under a chunky red knit beanie with a red pom-pom. He wears a knee-length brown hooded duffle coat with toggles, blue jeans and bright green rubber boots.
- **Grandpa:** a tall, gentle older man with short white hair who matches the character sheet reference. He wears a red-and-black buffalo-plaid flannel shirt, brown suspenders, grey work trousers and brown leather boots.
- **Mouse:** a tiny soft-grey field mouse with big round pink ears, a pink nose and a long thin tail. It stands upright, curious and cheerful.
- **Donkey:** a small grey donkey with a pale muzzle and belly, tall dark-tipped ears, a dark mane stripe and kind droopy eyes.
- **Cow:** a chunky chocolate-brown cow with short cream horns and a friendly broad face.
- **Sheep:** round, fluffy cream sheep with tight curly wool and soft pale faces.
- **Grandma Sheep:** an older cream ewe with a greyer woolly topknot and tiny round wire spectacles. She looks wise and amused.
- **Mary:** a young woman with a gentle face, a dusty-blue headscarf over a white under-veil, an oatmeal linen dress and a blue sash.
- **Joseph:** a sturdy young man with a short dark beard, a cream headcloth, a brown wool robe, a rope belt and sandals.
- **Angels of the host:** tall, majestic figures made of white-gold light. Their robes flow, their wings are huge and soft, and their faces are serene and only lightly drawn. They are glowing, not cute and not babyish.

### Avoid (negative prompt)
- Two or more scenes in one frame: no split panels, inset panels or collage.
- White margins, or vignette, cloud-shaped or torn-paper edges.
- Blurred, smeared or stretched filler areas.
- Figures cut off at the frame edge.
- Crowds or tiny background figures. More than four main figures.
- Any text, letters, signs or speech bubbles.
- Doubled heads, extra hands or fingers, merged animals, a floating lantern with no one holding it.
- Photorealism, glossy 3D, anime, neon, cold grey moods.
- Leo drawn off-model: wrong hat, missing green boots or an older face.

### Wall openings (put these after the style guide)
- **Center:** "Landscape 5:4. All main characters are well inside the frame, faces toward the viewer. The top 28% of the picture is a quiet, softly textured, mid-to-deep-value area (night sky, shadowed rafters or a dusk wash) with no faces, heads, hats, halos, hands, lanterns or focal objects. All heads sit below one-third of the height. Floor line about two-thirds down."
- **Side:** "Portrait 3:4. Scenery only, no people. Floor or horizon line about two-thirds down. The light comes from the [left/right] side of the frame, toward the center of the room. The outer edge is gently darker. Full-bleed."

### Per screen
Screen 3 stays as is. On each side wall, use **[right]** for the left wall's light direction and **[left]** for the right wall's.

**1 · Grandpa's barn (snowy dusk, cold blue with warm barn light)**
- L: A big snow-dusted pine tree at dusk on a farm, sticky brown pine cones hanging from its branches, and a lit farmhouse window far behind.
- C: At the open barn door at dusk, Leo hugs a huge armful of hay and holds up a sticky brown pine cone with delight. Grandpa smiles down at him, and a glowing lantern hangs on the doorpost.
- R: Inside the barn, a deep, inviting hay pile glows under a lantern on the plank wall. A cow and a donkey doze in their stalls.
- **C-sin:** the same, but Leo holds up a handful of golden hay instead of the pine cone.

**2 · The barn wakes up (the dream begins, gold)**
- L: Barn stalls where the cow and a sheep peek out over the rails. The loose hay is turning shimmering gold, with tiny sparks of light floating up.
- C: Leo sits up in glowing golden hay, wide-eyed and delighted, reaching for the lantern. The mouse stands on the toe of his green boot with its arms flung wide. Leo is in three-quarter view.
- R: The big barn door swings open onto a starry night, with golden light spilling out across the snow.

**4 · No room (night street, three shut doors)**
- L: A narrow Bethlehem street at night: a closed wooden door and dark shuttered windows in a stone wall.
- C: Joseph knocks on a heavy inn door while an innkeeper leans out shaking his head. Mary waits on the grey donkey, tired and hopeful, and Leo stands beside Joseph holding the lantern high.
- R: Another shut door. The street drops away downhill toward a faint warm glow from a small stable at the edge of town.

**5 · Even in this stable (warm lantern gold)**
- L: The chocolate-brown cow at its stall in a humble stone-and-timber stable, looking toward the center warmly, with hay bales stacked by the wall.
- C: One wooden manger where newborn baby Jesus sleeps on hay, swaddled in cream cloth and softly glowing. Mary and Joseph kneel beside it, and Leo kneels at the other end, setting his pine cone on the hay beside the baby's bed.
- R: The open stable door with one bright star overhead and sheep on a distant dark hill.
- **C-sin:** Leo smooths and tucks the soft hay around the edge of the baby's bed, with nothing in his hands.

**6 · Fear not (night hillside, burst of light)**
- L: A dark moonlit hillside with round cream sheep munching grass beside a low stone wall.
- C: A majestic angel of white-gold light bursts into the night sky above the hillside, and three shepherds tumble backward in surprise. In the foreground Leo kneels hugging a fluffy sheep, eyes closed, whispering into its woolly ear.
- R: The hill falls away to the tiny lights of Bethlehem far below, with a dropped shepherd's crook lying in the grass.

**7 · Not this sheep (sky full of angels)**
- L: Rows of radiant angels of light rise over dark hills. Every figure is fully inside the frame, with no figure touching any edge.
- C: Three shepherds and Leo sit by a small campfire gazing up in awe. Grandma Sheep stands on a rock beside them, looking up through her spectacles and counting on one raised hoof. Glowing angels fill the sky above, kept small enough that none is cut off.
- R: Mirrors the left wall: more rows of radiant angels over the hills, fully inside the frame.

**8 · Emmanuel (deep blue hush)**
- L: The stable in deep blue hush: the ox and a sheep asleep in the hay under a dim lantern.
- C: Hushed and golden: baby Jesus sleeps in the hay-filled manger, and Leo kneels close, gazing down with wonder. Mary sits softly behind.
- R: Grandpa's empty barn at the edge of dawn: a hay bed in the shape of a small boy under a hanging lantern.

**9 · Something wild (barn at dawn, blue snow light)**
- L: The barn at dawn, with a frosty window and the animals stirring in their stalls.
- C: In Grandpa's barn, a fluffy sheep munches the hay right beside Leo's head, and Leo sits up laughing. Grandpa kneels on the hay holding a lantern close, beaming. A pine cone lies in the hay beside Leo's pillow-dent. All faces are visible.
- R: The open barn door onto a snowy farmyard with the big pine tree outside.
- **C-sin:** the same, without the pine cone.

**10 · Softly as the snow (darkest screen, for the candle moment)**
- L: Inside the barn, the cow, donkey, sheep and mouse sleep curled together in golden hay beneath a softly glowing lantern.
- C: Outside in the snowy night, Leo ties a red ribbon on his pine cone and hangs it on a little snow-dusted pine tree. Grandpa holds the lantern up beside him, both smiling, with stars above. Keep the overall image dim.
- R: A dark snowy field under a deep, quiet starry sky. This is the darkest wall of the show.
- **C-sin:** Leo ties the red ribbon bow directly onto a branch of the little pine.

### Count
- 27 wall paintings, plus 4 no-pine-cone centers and the cover.
- At two takes each, about 64 images.
- At Artlist's last price (400 credits per image), that is about 25,600 credits. Running one take of each side wall and two of each center brings it to about 19,000.
- A cheaper option is to make the side walls first at one take each (they are simple scenery), then spend the second takes on the centers.

## Open questions for Chase
1. **Credits:** OK to spend that many Artlist credits (you had 70,450)?
2. **Text placement:** the text adviser and the layout adviser disagreed. This plan puts the answer on the **center top**, with a quiet band saved for it in the art. The old fix moved text to the sides only because the placeholder art had faces at the top.
3. **Screen 3 side walls:** the Drive frames have the old bubbles burned in. The clean side-wall art is on the home computer (`christmas-eve-book/stage/raw`). Otherwise those two walls need regenerating.
