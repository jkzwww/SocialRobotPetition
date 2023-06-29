<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Survey" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="admonishment" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="logical" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="authority" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="consistency" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="creditability" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="freedom" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="inquiry" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="main" src="html/javascripts/main.js" />
        <File name="main.min" src="html/javascripts/main.min.js" />
        <File name="polyfill" src="html/javascripts/polyfill.js" />
        <File name="polyfill.min" src="html/javascripts/polyfill.min.js" />
        <File name="Raleway-Black" src="html/styles/fonts/Raleway-Black.ttf" />
        <File name="Raleway-Regular" src="html/styles/fonts/Raleway-Regular.ttf" />
        <File name="main" src="html/styles/main.css" />
        <File name="index" src="html/index.html" />
        <File name="icon" src="icon.png" />
        <File name="service" src="service.py" />
        <File name="README" src="README.md" />
        <File name="Monash_Logo" src="html/Monash_Logo.jpg" />
        <File name="calc" src="html/javascripts/calc.js" />
        <File name="angry" src="html/styles/images/angry.png" />
        <File name="earth" src="html/styles/images/earth.png" />
        <File name="factory" src="html/styles/images/factory.png" />
        <File name="happy" src="html/styles/images/happy.png" />
        <File name="neutral" src="html/styles/images/neutral.png" />
        <File name="polarbear" src="html/styles/images/polarbear.png" />
        <File name="sad" src="html/styles/images/sad.png" />
        <File name="saveplanet" src="html/styles/images/saveplanet.png" />
        <File name="smile" src="html/styles/images/smile.png" />
        <File name="sos" src="html/styles/images/sos.png" />
        <File name="stopchange" src="html/styles/images/stopchange.png" />
        <File name="testing" src="testing.js" />
        <File name="data_processor" src="data_processor.py" />
        <File name="factory" src="html/factory.png" />
        <File name="planetStats" src="html/planetStats.png" />
        <File name="ipccMainPage" src="html/ipccMainPage.png" />
        <File name="draftIndex" src="html/draftIndex.html" />
        <File name="respList" src="dataRecord/respList.csv" />
        <File name="respSum" src="dataRecord/respSum.csv" />
        <File name="CCposter" src="html/CCposter.jpg" />
        <File name="sum_processor" src="sum_processor.py" />
        <File name="t1_0525_admonishment" src="testRawData/t1_0525_admonishment.csv" />
        <File name="t2_0601_logical" src="testRawData/t2_0601_logical.csv" />
        <File name="t3_0622_creditability" src="testRawData/t3_0622_creditability.csv" />
        <File name="smiley" src="html/styles/images/smiley.png" />
    </Resources>
    <Topics />
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
    <service name="service" autorun="true" execStart="./python service.py" />
    <executableFiles>
        <file path="python" />
    </executableFiles>
    <qipython name="service" />
</Package>
