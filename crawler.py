import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the names or titles you're looking for as a list
search_names = ["4-H Agent", "Colquitt County 4-H Educator", "Office / Clerical Assistant",
                "County Extension Agent - 4-H", "Administrative Assistant", "County Extension Coordinator",
                "County Extension Educator - 4-H", "County Extension Agent - ANR", "FACS Educator",
                "Public Service Professional", "County Extension Agent - FACS", "4-H Youth Development Agent",
                "4-H Educator", "4-H Laurens County AmeriCorps",
                "4H Program Assistant",
                "4-H Program Specialist",
                "4-H Tift County AmeriCorps State Member",
                "4-H Youth Extension Educator",
                "4-H/ANR Program Assistant",
                "Administrative Assistant (ANR Clerk)",
                "AG & Natural Resources Agent",
                "Agriculture Specialist",
                "AmeriCorps 4-H",
                "ANR Agent",
                "ANR Agent - County Coordinator",
                "ANR Educator",
                "ANR Program Assistant",
                "ANR/4-H Agent",
                "ANR/Master Gardner Program Assistant",
                "Bleckley County Program Assistant - 4-H",
                "Brooks County ANR Agent",
                "Bryan County 4-H Agent",
                "Bulloch County 4-H Educator",
                "Burke County 4-H Educator",
                "CEC and County Extension Agent - ANR",
                "Coffee County 4-H Educator",
                "Coffee County 4-H Program Assistant",
                "Colquitt County 4-H Educator",
                "Colquitt County Extension 4-H Agent",
                "Columbia County 4-H Educator",
                "Columbia County 4-H Program Assistant",
                "Cook Co 4-H Agent",
                "County 4-H Agent",
                "County 4-H Educator",
                "County Agent",
                "County Agent - Family and Consumer Sciences",
                "County Extension 4-H Agent",
                "County Extension 4-H Educator",
                "County Extension 4-H Program Assistant",
                "County Extension Agent",
                "County Extension Agent - 4-H",
                "County Extension Agent - ANR",
                "County Extension Agent - FACS",
                "County Extension Agent - FACS/CEC",
                "County Extension Agent - FACS/EFNEP",
                "County Extension Agent- 4-H",
                "County Extension Agent ANR",
                "County Extension Agent, 4-H Youth",
                "County Extension Agent, CP Pay Retire Rehire",
                "County Extension Agent, FACS",
                "County Extension ANR Agent",
                "County Extension ANR Vegetable Agent",
                "County Extension Associate - 4-H",
                "County Extension Coordinator and 4-H Youth Development Agent",
                "County Extension Coordinator- ANR",
                "County Extension Coordinator/4-H Agent",
                "County Extension Coordinator/Agent - 4-H",
                "County Extension Coordinator/Agent: 4-H",
                "County Extension Coordinator/ANR Agent", "County Extension ANR Vegetable Agent",
                "County Extension Associate - 4-H",
                "County Extension Coordinator and 4-H Youth Development Agent",
                "County Extension Coordinator- ANR",
                "County Extension Coordinator/4-H Agent",
                "County Extension Coordinator/Agent - 4-H",
                "County Extension Coordinator/Agent: 4-H",
                "County Extension Coordinator/ANR Agent",
                "County Extension Coordinator/FACS Agent",
                "County Extension Coordinator-ANR",
                "County Extension Educator - 4-H",
                "County Extension Educator, 4-H",
                "County Extension Program Assistant, 4-H",
                "County Extension Program Assistant,4-H Youth",
                "County Extension Secretary & Program Assistant, 4-H",
                "Crisp County Extension Agent / Entomology Graduate Student",
                "Crisp County FACS Agent",
                "Dawson County Extension Coordinator/Lumpkin ANR Agent"]

# Define the base URLs to search as a list
base_urls = [
    "https://extension.uga.edu",
    "https://site.extension.uga.edu/aaecext",
    "https://site.caes.uga.edu/anthfood",
    "https://intranet.caes.uga.edu/extension-resources/reporting/reporting-procedures-gacounts/help-menu/",
    "https://site.extension.uga.edu/applingcrop",
    "https://site.extension.uga.edu/beef",
    "https://site.caes.uga.edu/blueberry",
    "https://site.extension.uga.edu/brooksag",
    "https://site.extension.uga.edu/bullochag",
    "https://site.extension.uga.edu/burke",
    "https://site.caes.uga.edu/burkelab",
    "https://www.caes.uga.edu/about/jobs.html",
    "https://agecon.uga.edu/",
    "https://alec.caes.uga.edu",
    "https://animaldairy.uga.edu",
    "https://cropsoil.uga.edu/",
    "https://ent.uga.edu/",
    "https://foodscience.caes.uga.edu/",
    "https://hort.caes.uga.edu/",
    "https://plantpath.caes.uga.edu/",
    "https://poultry.caes.uga.edu/",
    "https://www.caes.uga.edu/extension-outreach/commodities.html",
    "https://beef.caes.uga.edu/",
    "https://turf.caes.uga.edu/",
    "https://muscadines.caes.uga.edu/",
    "https://pecanbreeding.uga.edu/",
    "https://tobacco.caes.uga.edu/",
    "https://www.caes.uga.edu/departments/international-programs.html",
    "https://caed.uga.edu",
    "https://cfs.caes.uga.edu",
    "https://www.caes.uga.edu/departments/griffin-campus.html",
    "https://eowaterlab.caes.uga.edu/",
    "https://site.extension.uga.edu/cherokee",
    "https://site.extension.uga.edu/climate",
    "https://coastalbg.uga.edu/",
    "https://site.extension.uga.edu/colquittag",
    "https://site.extension.uga.edu/cook",
    "https://site.extension.uga.edu/dairy",
    "https://site.extension.uga.edu/dooly",
    "https://site.caes.uga.edu/entoclub",
    "https://site.caes.uga.edu/envirotron",
    "https://www.caes.uga.edu/events/awfd",
    "https://extension.uga.edu/programs-services/georgia-master-gardener-extension-volunteer-program.html",
    "https://extension.uga.edu/programs-services/pesticide-safety-education.html",
    "https://extension.uga.edu/programs-services/school-garden-resources.html",
    "https://extension.uga.edu/programs-services/science-behind-our-food.html",
    "https://site.extension.uga.edu/fayette",
    "https://site.caes.uga.edu/foodenglab",
    "https://site.extension.uga.edu/forageteam",
    "https://site.extension.uga.edu/franklin",
    "https://site.extension.uga.edu/gacaa",
    "https://site.caes.uga.edu/georgiaturf",
    "https://site.caes.uga.edu/ges",
    "https://site.extension.uga.edu/gnc",
    "https://site.extension.uga.edu/ipm",
    "https://site.caes.uga.edu/kvitkolab",
    "https://site.extension.uga.edu/laurens",
    "https://site.caes.uga.edu/lbcap",
    "https://site.extension.uga.edu/lowndesecholsag",
    "https://site.caes.uga.edu/mchughlab",
    "https://site.extension.uga.edu/mgevp",
    "https://site.extension.uga.edu/military",
    "https://site.caes.uga.edu/mycologylab",
    "https://site.extension.uga.edu/oliverlab",
    "https://site.extension.uga.edu/peaches",
    "https://site.extension.uga.edu/peanutent",
    "https://site.extension.uga.edu/pecan",
    "https://site.extension.uga.edu/plowpoints",
    "https://site.caes.uga.edu/ftfpeanutlab",
    "https://site.extension.uga.edu/poultrytips",
    "https://site.caes.uga.edu/schmidtlab",
    "https://site.caes.uga.edu/sehaycontest",
    "https://site.caes.uga.edu/sehp",
    "https://soils.uga.edu/",
    "https://southernoutlook.caes.uga.edu",
    "https://site.caes.uga.edu/strandlab",
    "https://site.extension.uga.edu/strawberry",
    "https://www.caes.uga.edu/students.html",
    "https://site.caes.uga.edu/studyabroad",
    "https://site.extension.uga.edu/tattnall",
    "https://site.caes.uga.edu/tech",
    "https://thompsonlab.uga.edu/",
    "https://site.extension.uga.edu/threerivers",
    "https://site.caes.uga.edu/turfgrassbreeding",
    "https://site.caes.uga.edu/ugca",
    "https://site.caes.uga.edu/vegpath",
    "https://site.extension.uga.edu/viticulture",
    "https://site.caes.uga.edu/vogellab",
    "https://site.extension.uga.edu/water",
    "https://site.caes.uga.edu/whiteflies-tylcv",
    "https://site.extension.uga.edu/wilcoxcoag/",
    "https://site.caes.uga.edu/yanglab",
    "https://extension.uga.edu/county-offices/pickens.html",
    "https://aquaculture.caes.uga.edu/",
    "https://peaches.caes.uga.edu/",

    "https://peanuts.caes.uga.edu/",
    "https://pecans.uga.edu/",
    "https://gasoybeans.caes.uga.edu/",
    "https://vegetables.caes.uga.edu/",

    "https://sustainagga.caes.uga.edu/systems/conservation-tillage.html",
    "https://dwbrooks.caes.uga.edu/",
    "https://flavorofgeorgia.caes.uga.edu/",
    "https://tifton.caes.uga.edu",
    "https://ugatiftonconference.caes.uga.edu",
    "https://extension.uga.edu/county-offices/bacon.html",
    "https://extension.uga.edu/county-offices/baker.html",
    "https://extension.uga.edu/county-offices/baldwin.html",
    "https://extension.uga.edu/county-offices/banks.html",
    "https://extension.uga.edu/county-offices/barrow.html",
    "https://extension.uga.edu/county-offices/bartow.html",
    "https://extension.uga.edu/county-offices/benhill.html",
    "https://extension.uga.edu/county-offices/berrien.html",
    "https://extension.uga.edu/county-offices/bibb.html",
    "https://extension.uga.edu/county-offices/bleckley.html",
    "https://extension.uga.edu/county-offices/brantley.html",
    "https://extension.uga.edu/county-offices/brooks.html",
    "https://extension.uga.edu/county-offices/bryan.html",
    "https://extension.uga.edu/county-offices/bulloch.html",
    "https://extension.uga.edu/county-offices/burke.html",
    "https://extension.uga.edu/county-offices/butts.html",
    "https://extension.uga.edu/county-offices/calhoun.html",
    "https://extension.uga.edu/county-offices/camden.html",
    "https://extension.uga.edu/county-offices/candler.html",
    "https://extension.uga.edu/county-offices/carroll.html",
    "https://extension.uga.edu/county-offices/catoosa.html",
    "https://extension.uga.edu/county-offices/charlton.html",
    "https://extension.uga.edu/county-offices/chatham.html",
    "https://extension.uga.edu/county-offices/chattahoochee.html",
    "https://extension.uga.edu/county-offices/chattooga.html",
    "https://extension.uga.edu/county-offices/cherokee.html",
    "https://extension.uga.edu/county-offices/clay.html",
    "https://extension.uga.edu/county-offices/clayton.html",
    "https://extension.uga.edu/county-offices/clinch.html",
    "https://extension.uga.edu/county-offices/cobb.html",
    "https://extension.uga.edu/county-offices/coffee.html",
    "https://extension.uga.edu/county-offices/colquitt.html",
    "https://extension.uga.edu/county-offices/columbia.html",
    "https://extension.uga.edu/county-offices/cook.html",
    "https://extension.uga.edu/county-offices/coweta.html",
    "https://extension.uga.edu/county-offices/crawford.html",
    "https://extension.uga.edu/county-offices/crisp.html",
    "https://extension.uga.edu/county-offices/dade.html",
    "https://extension.uga.edu/county-offices/dawson.html",
    "https://extension.uga.edu/county-offices/decatur.html",
    "https://extension.uga.edu/county-offices/dekalb.html",
    "https://extension.uga.edu/county-offices/dodge.html",
    "https://extension.uga.edu/county-offices/dooly.html",
    "https://extension.uga.edu/county-offices/dougherty.html",
    "https://extension.uga.edu/county-offices/douglas.html",
    "https://extension.uga.edu/county-offices/early.html",
    "https://extension.uga.edu/county-offices/echols.html",
    "https://extension.uga.edu/county-offices/effingham.html",
    "https://extension.uga.edu/county-offices/elbert.html",
    "https://extension.uga.edu/county-offices/emanuel.html",
    "https://extension.uga.edu/county-offices/evans.html",
    "https://extension.uga.edu/county-offices/fannin.html",
    "https://extension.uga.edu/county-offices/fayette.html",
    "https://extension.uga.edu/county-offices/floyd.html",
    "https://extension.uga.edu/county-offices/forsyth.html",
    "https://extension.uga.edu/county-offices/franklin.html",
    "https://extension.uga.edu/county-offices/fulton.html",
    "https://extension.uga.edu/county-offices/gilmer.html",
    "https://extension.uga.edu/county-offices/glascock.html",
    "https://extension.uga.edu/county-offices/glynn.html",
    "https://extension.uga.edu/county-offices/gordon.html",
    "https://extension.uga.edu/county-offices/grady.html",
    "https://extension.uga.edu/county-offices/greene.html",
    "https://extension.uga.edu/county-offices/gwinnett.html",
    "https://extension.uga.edu/county-offices/habersham.html",
    "https://extension.uga.edu/county-offices/hall.html",
    "https://extension.uga.edu/county-offices/hancock.html",
    "https://extension.uga.edu/county-offices/haralson.html",
    "https://extension.uga.edu/county-offices/harris.html",
    "https://extension.uga.edu/county-offices/hart.html",
    "https://extension.uga.edu/county-offices/heard.html",
    "https://extension.uga.edu/county-offices/henry.html",
    "https://extension.uga.edu/county-offices/houston.html",
    "https://extension.uga.edu/county-offices/irwin.html",
    "https://extension.uga.edu/county-offices/jackson.html",
    "https://extension.uga.edu/county-offices/jasper.html",
    "https://extension.uga.edu/county-offices/jeffdavis.html",
    "https://extension.uga.edu/county-offices/jefferson.html",
    "https://extension.uga.edu/county-offices/jenkins.html",
    "https://extension.uga.edu/county-offices/johnson.html",
    "https://extension.uga.edu/county-offices/jones.html",
    "https://extension.uga.edu/county-offices/lamar.html",
    "https://extension.uga.edu/county-offices/lanier.html",
    "https://extension.uga.edu/county-offices/laurens.html",
    "https://extension.uga.edu/county-offices/lee.html",
    "https://extension.uga.edu/county-offices/liberty.html",
    "https://extension.uga.edu/county-offices/lincoln.html",
    "https://extension.uga.edu/county-offices/long.html",
    "https://extension.uga.edu/county-offices/lowndes.html",
    "https://extension.uga.edu/county-offices/lumpkin.html",
    "https://extension.uga.edu/county-offices/macon.html",
    "https://extension.uga.edu/county-offices/madison.html",
    "https://extension.uga.edu/county-offices/marion.html",
    "https://extension.uga.edu/county-offices/mcduffie.html",
    "https://extension.uga.edu/county-offices/mcintosh.html",
    "https://extension.uga.edu/county-offices/meriwether.html",
    "https://extension.uga.edu/county-offices/miller.html",
    "https://extension.uga.edu/county-offices/mitchell.html",
    "https://extension.uga.edu/county-offices/monroe.html",
    "https://extension.uga.edu/county-offices/montgomery.html",
    "https://extension.uga.edu/county-offices/morgan.html",
    "https://extension.uga.edu/county-offices/murray.html",
    "https://extension.uga.edu/county-offices/muscogee.html",
    "https://extension.uga.edu/county-offices/newton.html",
    "https://extension.uga.edu/county-offices/oconee.html",
    "https://extension.uga.edu/county-offices/oglethorpe.html",
    "https://extension.uga.edu/county-offices/paulding.html",
    "https://extension.uga.edu/county-offices/peach.html",
    "https://extension.uga.edu/county-offices/pierce.html",
    "https://extension.uga.edu/county-offices/pike.html",
    "https://extension.uga.edu/county-offices/polk.html",
    "https://extension.uga.edu/county-offices/pulaski.html",
    "https://extension.uga.edu/county-offices/putnam.html",
    "https://extension.uga.edu/county-offices/quitman.html",
    "https://extension.uga.edu/county-offices/rabun.html",
    "https://extension.uga.edu/county-offices/randolph.html",
    "https://extension.uga.edu/county-offices/rockdale.html",
    "https://extension.uga.edu/county-offices/schley.html",
    "https://extension.uga.edu/county-offices/screven.html",
    "https://extension.uga.edu/county-offices/seminole.html",
    "https://extension.uga.edu/county-offices/spalding.html",
    "https://extension.uga.edu/county-offices/stephens.html",
    "https://extension.uga.edu/county-offices/stewart.html",
    "https://extension.uga.edu/county-offices/sumter.html",
    "https://extension.uga.edu/county-offices/talbot.html",
    "https://extension.uga.edu/county-offices/tattnall.html",
    "https://extension.uga.edu/county-offices/taylor.html",
    "https://extension.uga.edu/county-offices/telfair.html",
    "https://extension.uga.edu/county-offices/terrell.html",
    "https://extension.uga.edu/county-offices/thomas.html",
    "https://extension.uga.edu/county-offices/tift.html",
    "https://extension.uga.edu/county-offices/toombs.html",
    "https://extension.uga.edu/county-offices/towns.html",
    "https://extension.uga.edu/county-offices/treutlen.html",
    "https://extension.uga.edu/county-offices/troup.html",
    "https://extension.uga.edu/county-offices/turner.html",
    "https://extension.uga.edu/county-offices/twiggs.html",
    "https://extension.uga.edu/county-offices/union.html",
    "https://extension.uga.edu/county-offices/upson.html",
    "https://extension.uga.edu/county-offices/walker.html",
    "https://extension.uga.edu/county-offices/walton.html",
    "https://extension.uga.edu/county-offices/ware.html",
    "https://extension.uga.edu/county-offices/warren.html",
    "https://extension.uga.edu/county-offices/washington.html",
    "https://extension.uga.edu/county-offices/wayne.html",
    "https://extension.uga.edu/county-offices/webster.html",
    "https://extension.uga.edu/county-offices/wheeler.html",
    "https://extension.uga.edu/county-offices/white.html",
    "https://extension.uga.edu/county-offices/whitfield.html",
    "https://extension.uga.edu/county-offices/wilcox.html",
    "https://extension.uga.edu/county-offices/wilkes.html",
    "https://extension.uga.edu/county-offices/wilkinson.html",
    "https://extension.uga.edu/county-offices/worth.html",
    "https://extension.uga.edu/county-offices/taliaferro.html",
    "https://extension.uga.edu/county-offices/richmond.html",
    "https://site.extension.uga.edu/turnerab/",
    "https://bees.caes.uga.edu",
    "https://extension.uga.edu/programs-services/integrated-pest-management.html",
    "https://site.extension.uga.edu/benhillcoag/",
    "https://site.extension.uga.edu/enlace/",
    "https://intranet.caes.uga.edu/",
    "https://extension.uga.edu/programs-services/food-science.html",
    "https://wildpeanutlab.uga.edu/",
    "https://site.caes.uga.edu/sec-lab/",
    "https://site.extension.uga.edu/fultonag/",
    "https://site.caes.uga.edu/fst/",
    "https://site.extension.uga.edu/thedirtonfloyd/",
    "https://site.extension.uga.edu/gordongrown/",
    "https://ftfpeanutlab.caes.uga.edu/",
    "https://site.caes.uga.edu/pecanentomlab/",
    "https://site.extension.uga.edu/bleckleyblog/",
    "https://beefsafety.caes.uga.edu/",
    "https://site.caes.uga.edu/expstatgrif/",
    "https://site.caes.uga.edu/entomologyresearch/",
    "https://site.caes.uga.edu/agdatascience/",
    "https://site.caes.uga.edu/alimdl/",
    "https://sustainagga.caes.uga.edu/",
    "https://georgiaforages.caes.uga.edu/",
    "https://site.extension.uga.edu/peqh/",
    "https://site.extension.uga.edu/burkeag/",
    "https://site.caes.uga.edu/esp/",
    "https://site.caes.uga.edu/carpophiline-id/",
    "https://site.caes.uga.edu/livestockarena/",
    "https://site.caes.uga.edu/soilmicro/",
    "https://site.caes.uga.edu/basingerlab",
    "https://site.caes.uga.edu/agl/",
    "https://agforecast.caes.uga.edu",
    "https://www.caes.uga.edu/alumni.html",
    "https://eowaterlab.caes.uga.edu/",
    "https://site.caes.uga.edu/pins/",
    "https://extension.uga.edu/programs-services/structural-pest-management.html",
    "https://intl-agday.caes.uga.edu",
    "https://grains.caes.uga.edu",
    "https://site.extension.uga.edu/laurensgarden/",
    "https://site.extension.uga.edu/calhounag/",
    "https://site.caes.uga.edu/library-griffin/",
    "https://site.caes.uga.edu/liwc/",
    "https://alec.caes.uga.edu/undergraduate/experiential-learning/focus.html",
    "https://site.caes.uga.edu/springbreaktour/",
    "https://napb2019.uga.edu/",
    "https://site.extension.uga.edu/worthag/",
    "https://site.extension.uga.edu/camdenanr/",
    "https://site.caes.uga.edu/chavezlab/",
    "https://site.extension.uga.edu/tattnall4h/",
    "https://site.extension.uga.edu/vidaliaonion/",
    "https://site.extension.uga.edu/doughertyhort/",
    "https://site.extension.uga.edu/sfsi/",
    "https://site.extension.uga.edu/tiftcoag/",
    "https://site.caes.uga.edu/blackflylab",
    "https://equine.caes.uga.edu",
    "https://site.caes.uga.edu/citrus/",
    "https://site.extension.uga.edu/murraygrown/",
    "https://espl.caes.uga.edu",
    "https://site.caes.uga.edu/ornapath",
    "https://site.extension.uga.edu/aware/",
    "https://omc.caes.uga.edu",
    "https://site.extension.uga.edu/bartow/",
    "https://site.extension.uga.edu/organic/",
    "https://olod.caes.uga.edu",
    "https://attapulgus.caes.uga.edu",
    "https://abo.caes.uga.edu/",
    "https://striplingpark.caes.uga.edu",
    "https://gamountain.caes.uga.edu",
    "https://jpcampbell.caes.uga.edu",
    "https://nwgeorgia.caes.uga.edu",
    "https://segeorgia.caes.uga.edu",
    "https://swgeorgia.caes.uga.edu",
    "https://site.caes.uga.edu/smartfoodprocessinglab/",
    "https://site.caes.uga.edu/agroecology/",
    "https://site.caes.uga.edu/yaoyaolab/",
    'https://site.extension.uga.edu/crispcoag/',
    'https://site.caes.uga.edu/esseililab/',
    'https://site.caes.uga.edu/smallfruitentolab/',
    'https://site.caes.uga.edu/mitchumlab/',
    'https://site.caes.uga.edu/trishjmoorelab/',
    'https://smallfruits.org/',
    'https://site.caes.uga.edu/duttalab/',
    'https://nambeesanlab.uga.edu/',
    'https://site.extension.uga.edu/maconcountyagnews/',
    'https://site.extension.uga.edu/lincoln/',
    'https://site.extension.uga.edu/paulding/',
    'https://site.extension.uga.edu/georgia4hscience/',
    'https://site.extension.uga.edu/bilingualopinions/',
    'https://site.caes.uga.edu/agedstudentteaching/',
    'https://site.extension.uga.edu/madison/',
    'https://site.caes.uga.edu/plantvirologylab/',
    'https://site.extension.uga.edu/newtonextanr/',
    'https://site.caes.uga.edu/hortjobs/',
    'https://extension.uga.edu/county-offices.html',
    'https://site.caes.uga.edu/fmlab/',
    'https://site.extension.uga.edu/evansag/',
    'https://site.extension.uga.edu/jackson4h/',
    'https://site.extension.uga.edu/effinghamanr/',
    'https://site.caes.uga.edu/itlelab/',
    'https://site.extension.uga.edu/postharvest/',
    'https://site.extension.uga.edu/fannin-gilmer/',
    'https://site.caes.uga.edu/ikassem/',
    'https://site.extension.uga.edu/georgiagreen/',
    'https://site.extension.uga.edu/precisionag/',
    'https://site.caes.uga.edu/ajmoorelab/',
    'https://site.caes.uga.edu/tnrrl/',
    'https://site.extension.uga.edu/barrowanr',
    'https://site.extension.uga.edu/lanierclinchag/',
    'https://site.caes.uga.edu/alumni/',
    'https://site.extension.uga.edu/anrep/',
    'https://site.extension.uga.edu/townsandunionag/',
    'https://site.extension.uga.edu/healthiertogether/',
    'https://site.extension.uga.edu/gapples/',
    'https://site.caes.uga.edu/bramanlab/',
    'https://site.caes.uga.edu/fsc/',
    'https://extension.uga.edu/',
    'https://site.extension.uga.edu/longcounty4h/',
    'https://site.caes.uga.edu/scriturf/',
    'https://site.extension.uga.edu/gardener/',
    "https://site.caes.uga.edu/srinivasanlab/",
    "https://site.extension.uga.edu/hie/",
    "https://site.extension.uga.edu/dbl/",
    "https://site.extension.uga.edu/extensionreads/",
    "https://site.caes.uga.edu/springbreak2019/",
    "https://site.extension.uga.edu/textiles/",
    "https://site.extension.uga.edu/pshp/",
    "https://extension.uga.edu/programs-services/radon-testing.html",
    "https://site.extension.uga.edu/extinterns/",
    "https://site.extension.uga.edu/jackson/",
    "https://site.extension.uga.edu/foodscene/",
    "https://site.extension.uga.edu/greenway/",
    "https://site.extension.uga.edu/project-find/",
    "https://site.caes.uga.edu/job-board/",
    "https://site.caes.uga.edu/lammlab/",
    "https://site.extension.uga.edu/colquitthomeowners/",
    "https://site.extension.uga.edu/eat-healthy-be-active/",
    "https://site.caes.uga.edu/hortscholarships/",
    "https://site.caes.uga.edu/springbreaktour/",
    "https://site.extension.uga.edu/eae/",
    'https://site.extension.uga.edu/seminoleag/',
    'https://site.caes.uga.edu/adsmeatstore/',
    'https://extension.uga.edu/about/join-our-team.html',
    'https://site.caes.uga.edu/jespersenlab/',
    'https://site.extension.uga.edu/preventopioidmisuse/',
    'https://site.caes.uga.edu/rcrlab/',
    'https://greenhouses.caes.uga.edu/',
    'https://site.caes.uga.edu/abg/',
    'https://site.extension.uga.edu/kbb/',
    'https://site.caes.uga.edu/best/',
    'https://site.caes.uga.edu/organichort/',
    'https://site.extension.uga.edu/ganrep/',
    'https://site.caes.uga.edu/smallfruits/',
    'https://site.caes.uga.edu/precisionpoultry/',
    'https://site.caes.uga.edu/yulab/',
    'https://site.caes.uga.edu/epuraeaocularis/',
    'https://site.caes.uga.edu/tiftonpostdocs/',
    'https://site.extension.uga.edu/fayette/',
    'https://site.extension.uga.edu/benhill4h/',
    'https://site.extension.uga.edu/thriving/',
    'https://psep.uga.edu',
    'https://site.extension.uga.edu/forsyth/',
    'https://site.extension.uga.edu/gardenwhereyouare/',
    'https://site.caes.uga.edu/sandlin/',
    'https://site.caes.uga.edu/josephlab/',
    'https://site.extension.uga.edu/gmanr/',
    'https://site.extension.uga.edu/camden4h/',
    'https://site.extension.uga.edu/oglethorpe/',
    'https://site.extension.uga.edu/foodscienceandtechnology/',
    'https://site.caes.uga.edu/griffin/']

# Open a file to write the search results
with open('results/search_results.txt', 'w') as f:
    # Loop through each base URL
    for base_url in base_urls:
        # Send a request to the base URL and get the HTML content
        try:
            response = requests.get(base_url)
            response.raise_for_status()
            html_content = response.content
        except requests.exceptions.RequestException as e:
            print(f"Could not retrieve {base_url}: {e}")
            continue  # Skip to the next base URL

        # Parse the HTML content using BeautifulSoup and extract all links from the page
        soup = BeautifulSoup(html_content, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]

        # Loop through each link and search for the search terms
        for link in links:
            # Combine the link with the base URL to create the full URL
            full_url = urljoin(base_url, link)

            # Send a request to the page and get the HTML content
            try:
                response = requests.get(full_url)
                response.raise_for_status()
                html_content = response.content
            except requests.exceptions.RequestException as e:
                print(f"Could not retrieve {full_url}: {e}")
                continue  # Skip to the next page

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Loop through each search term and write the results to a file if found
            for search_name in search_names:
                search_results = soup.find_all(string=lambda text: search_name.lower() in str(text).lower())
                if len(search_results) > 0:
                    f.write(f"\nSearch term '{search_name}' found on {full_url}:\n")
                    count = len(search_results)
                    f.write(f"\tFound {count} times.\n")
                    for result in search_results:
                        f.write(f"\t{result}\n")
                        print(f"{search_name} found on {full_url}: {result}")
