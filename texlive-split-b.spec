%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-b
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0355:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/around-the-bend.doc.tar.xz
Source0356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arphic.tar.xz
Source0357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arphic.doc.tar.xz
Source0358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arrayjobx.tar.xz
Source0359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arrayjobx.doc.tar.xz
Source0360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arraysort.tar.xz
Source0361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arraysort.doc.tar.xz
Source0363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arsclassica.tar.xz
Source0364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arsclassica.doc.tar.xz
Source0365:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/articleingud.tar.xz
Source0366:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/articleingud.doc.tar.xz
Source0368:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arydshln.tar.xz
Source0369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arydshln.doc.tar.xz
Source0371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asaetr.tar.xz
Source0372:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asaetr.doc.tar.xz
Source0375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascelike.tar.xz
Source0376:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascelike.doc.tar.xz
Source0377:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascii-chart.doc.tar.xz
Source0378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascii-font.tar.xz
Source0379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascii-font.doc.tar.xz
Source0381:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/askmaps.tar.xz
Source0382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/askmaps.doc.tar.xz
Source0383:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aspectratio.tar.xz
Source0384:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aspectratio.doc.tar.xz
Source0385:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/assignment.tar.xz
Source0386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/assignment.doc.tar.xz
Source0387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/assoccnt.tar.xz
Source0388:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/assoccnt.doc.tar.xz
Source0389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/astro.tar.xz
Source0390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/astro.doc.tar.xz
Source0391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asyfig.tar.xz
Source0392:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asyfig.doc.tar.xz
Source0394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asypictureb.tar.xz
Source0395:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asypictureb.doc.tar.xz
Source0397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/attachfile.tar.xz
Source0398:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/attachfile.doc.tar.xz
Source0400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/augie.tar.xz
Source0401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/augie.doc.tar.xz
Source0402:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/auncial-new.tar.xz
Source0403:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/auncial-new.doc.tar.xz
Source0405:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aurical.tar.xz
Source0406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aurical.doc.tar.xz
Source0407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/authoraftertitle.tar.xz
Source0408:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/authoraftertitle.doc.tar.xz
Source0411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autoarea.tar.xz
Source0412:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autoarea.doc.tar.xz
Source0413:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/automata.tar.xz
Source0414:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/automata.doc.tar.xz
Source0415:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autonum.tar.xz
Source0416:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autonum.doc.tar.xz
Source0418:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autopdf.tar.xz
Source0419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autopdf.doc.tar.xz
Source0421:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/auto-pst-pdf.tar.xz
Source0422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/auto-pst-pdf.doc.tar.xz
Source0424:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/avantgar.tar.xz
Source0425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/avremu.tar.xz
Source0426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/avremu.doc.tar.xz
Source0428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/b1encoding.tar.xz
Source0429:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/b1encoding.doc.tar.xz
Source0431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-albanian.tar.xz
Source0432:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-albanian.doc.tar.xz
Source0437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-basque.tar.xz
Source0438:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-basque.doc.tar.xz
Source0440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babelbib.tar.xz
Source0441:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babelbib.doc.tar.xz
Source0442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-bosnian.tar.xz
Source0443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-bosnian.doc.tar.xz
Source0445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-breton.tar.xz
Source0446:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-breton.doc.tar.xz
Source0448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-bulgarian.tar.xz
Source0449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-bulgarian.doc.tar.xz
Source0451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-catalan.tar.xz
Source0452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-catalan.doc.tar.xz
Source0454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-croatian.tar.xz
Source0455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-croatian.doc.tar.xz
Source0457:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-czech.tar.xz
Source0458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-czech.doc.tar.xz
Source0460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-danish.tar.xz
Source0461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-danish.doc.tar.xz
Source0463:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-dutch.tar.xz
Source0464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-dutch.doc.tar.xz
Source0466:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-english.tar.xz
Source0467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-english.doc.tar.xz
Source0469:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-esperanto.tar.xz
Source0470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-esperanto.doc.tar.xz
Source0472:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-estonian.tar.xz
Source0473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-estonian.doc.tar.xz
Source0475:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-finnish.tar.xz
Source0476:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-finnish.doc.tar.xz
Source0478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-french.tar.xz
Source0479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-french.doc.tar.xz
Source0481:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-friulan.tar.xz
Source0482:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-friulan.doc.tar.xz
Source0484:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-galician.tar.xz
Source0485:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-galician.doc.tar.xz
Source0487:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-georgian.tar.xz
Source0488:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-georgian.doc.tar.xz
Source0489:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-german.tar.xz
Source0490:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-german.doc.tar.xz
Source0492:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-greek.tar.xz
Source0493:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-greek.doc.tar.xz
Source0495:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-hebrew.tar.xz
Source0496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-hebrew.doc.tar.xz
Source0498:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-hungarian.tar.xz
Source0499:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-hungarian.doc.tar.xz
Source0500:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-icelandic.tar.xz
Source0501:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-icelandic.doc.tar.xz
Source0503:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-interlingua.tar.xz
Source0504:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-interlingua.doc.tar.xz
Source0506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-irish.tar.xz
Source0507:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-irish.doc.tar.xz
Source0509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-italian.tar.xz
Source0510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-italian.doc.tar.xz
Source0512:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-kurmanji.tar.xz
Source0513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-kurmanji.doc.tar.xz
Source0515:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-latin.tar.xz
Source0516:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-latin.doc.tar.xz
Source0518:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-latvian.tar.xz
Source0519:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-latvian.doc.tar.xz
Source0521:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-norsk.tar.xz
Source0522:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-norsk.doc.tar.xz
Source0524:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-piedmontese.tar.xz
Source0525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-piedmontese.doc.tar.xz
Source0527:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-polish.tar.xz
Source0528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-polish.doc.tar.xz
Source0530:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-portuges.tar.xz
Source0531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-portuges.doc.tar.xz
Source0533:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-romanian.tar.xz
Source0534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-romanian.doc.tar.xz
Source0536:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-romansh.tar.xz
Source0537:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-romansh.doc.tar.xz
Source0539:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-russian.tar.xz
Source0540:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-russian.doc.tar.xz
Source0542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-samin.tar.xz
Source0543:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-samin.doc.tar.xz
Source0545:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-scottish.tar.xz
Source0546:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-scottish.doc.tar.xz
Source0548:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-serbianc.tar.xz
Source0549:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-serbianc.doc.tar.xz
Source0551:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-serbian.tar.xz
Source0552:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-serbian.doc.tar.xz
Source0554:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-slovak.tar.xz
Source0555:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-slovak.doc.tar.xz
Source0557:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-slovenian.tar.xz
Source0558:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-slovenian.doc.tar.xz
Source0560:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-sorbian.tar.xz
Source0561:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-sorbian.doc.tar.xz
Source0563:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-spanglish.tar.xz
Source0564:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-spanglish.doc.tar.xz
Source0565:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-spanish.tar.xz
Source0566:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-spanish.doc.tar.xz
Source0568:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-swedish.tar.xz
Source0569:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-swedish.doc.tar.xz
Source0571:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-thai.tar.xz
Source0572:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-thai.doc.tar.xz
Source0574:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel.tar.xz
Source0575:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel.doc.tar.xz
Source0577:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-turkish.tar.xz
Source0578:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-turkish.doc.tar.xz
Source0580:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-ukrainian.tar.xz
Source0581:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-ukrainian.doc.tar.xz
Source0583:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-vietnamese.tar.xz
Source0585:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-welsh.tar.xz
Source0586:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-welsh.doc.tar.xz
Source0588:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/background.tar.xz
Source0589:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/background.doc.tar.xz
Source0591:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/backnaur.tar.xz
Source0592:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/backnaur.doc.tar.xz
Source0594:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bagpipe.tar.xz
Source0595:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bagpipe.doc.tar.xz
Source0596:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bangorcsthesis.tar.xz
Source0597:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bangorcsthesis.doc.tar.xz
Source0599:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bangtex.tar.xz
Source0600:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bangtex.doc.tar.xz
Source0601:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bankstatement.tar.xz
Source0602:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bankstatement.doc.tar.xz
Source0603:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/barcodes.tar.xz
Source0604:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/barcodes.doc.tar.xz
Source0606:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bardiag.tar.xz
Source0607:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bardiag.doc.tar.xz
Source0608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/barr.tar.xz
Source0609:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/barr.doc.tar.xz
Source0610:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bartel-chess-fonts.tar.xz
Source0611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bartel-chess-fonts.doc.tar.xz
Source0612:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bashful.tar.xz
Source0613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bashful.doc.tar.xz
Source0614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/basicarith.tar.xz
Source0615:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/basicarith.doc.tar.xz
Source0617:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baskervald.tar.xz
Source0618:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baskervald.doc.tar.xz
Source0620:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baskervaldx.tar.xz
Source0621:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baskervaldx.doc.tar.xz
Source0622:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/basque-book.tar.xz
Source0623:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/basque-book.doc.tar.xz
Source0625:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/basque-date.tar.xz
Source0626:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/basque-date.doc.tar.xz
Source0628:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbcard.tar.xz
Source0629:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bbcard.doc.tar.xz
Source7226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asapsym.tar.xz
Source7227:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asapsym.doc.tar.xz
Source7229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asciilist.tar.xz
Source7230:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asciilist.doc.tar.xz
Source7232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-belarusian.tar.xz
Source7233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-belarusian.doc.tar.xz
Source7235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-macedonian.tar.xz
Source7236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-macedonian.doc.tar.xz
Source7238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-occitan.tar.xz
Source7239:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-occitan.doc.tar.xz
Source7241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-vietnamese.doc.tar.xz
Source7609:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-indonesian.tar.xz
Source7610:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-indonesian.doc.tar.xz
Source7611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-malay.tar.xz
Source7612:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-malay.doc.tar.xz
Source7631:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arphic-ttf.tar.xz
Source7632:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arphic-ttf.doc.tar.xz
Source7633:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asymptote-by-example-zh-cn.doc.tar.xz
Source7634:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asymptote-faq-zh-cn.doc.tar.xz
Source7635:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/asymptote-manual-zh-cn.doc.tar.xz
Source7636:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aucklandthesis.tar.xz
Source7637:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aucklandthesis.doc.tar.xz
Source7638:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aurl.tar.xz
Source7639:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aurl.doc.tar.xz
Source7640:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/awesomebox.tar.xz
Source7641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/awesomebox.doc.tar.xz
Source7642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-azerbaijani.tar.xz
Source7643:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-azerbaijani.doc.tar.xz
Source7644:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baekmuk.tar.xz
Source7645:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baekmuk.doc.tar.xz
Source7646:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bangorexam.tar.xz
Source7647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bangorexam.doc.tar.xz
Source7648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baskervillef.tar.xz
Source7649:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/baskervillef.doc.tar.xz
Source8036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autoaligne.doc.tar.xz
Source8037:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autoaligne.tar.xz
Source8064:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascmac.tar.xz
Source8065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ascmac.doc.tar.xz
Source8066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/authorarchive.tar.xz
Source8067:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/authorarchive.doc.tar.xz
Source8068:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autobreak.tar.xz
Source8069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autobreak.doc.tar.xz
Source8070:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/auto-pst-pdf-lua.tar.xz
Source8071:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/auto-pst-pdf-lua.doc.tar.xz
Source8074:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-japanese.tar.xz
Source8075:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/babel-japanese.doc.tar.xz
Source8076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bath-bst.tar.xz
Source8077:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bath-bst.doc.tar.xz


%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-around-the-bend-doc
Summary:        Documentation for around-the-bend
Version:        svn15878.0

Provides:       tex-around-the-bend-doc
AutoReqProv:    No

%description -n texlive-around-the-bend-doc
Documentation for around-the-bend

%package -n texlive-arphic
Provides:       tex-arphic = %{tl_version}
License:        Arphic
Summary:        Arphic (Chinese) font packages
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(bkaiu.map) = %{tl_version}, tex(bsmiu.map) = %{tl_version}
Provides:       tex(gbsnu.map) = %{tl_version}, tex(gkaiu.map) = %{tl_version}
Provides:       tex(bkaimp00.tfm) = %{tl_version}, tex(bkaimp01.tfm) = %{tl_version}
Provides:       tex(bkaimp02.tfm) = %{tl_version}, tex(bkaimp03.tfm) = %{tl_version}
Provides:       tex(bkaimp04.tfm) = %{tl_version}, tex(bkaimp05.tfm) = %{tl_version}
Provides:       tex(bkaimp06.tfm) = %{tl_version}, tex(bkaimp07.tfm) = %{tl_version}
Provides:       tex(bkaimp08.tfm) = %{tl_version}, tex(bkaimp09.tfm) = %{tl_version}
Provides:       tex(bkaimp10.tfm) = %{tl_version}, tex(bkaimp11.tfm) = %{tl_version}
Provides:       tex(bkaimp12.tfm) = %{tl_version}, tex(bkaimp13.tfm) = %{tl_version}
Provides:       tex(bkaimp14.tfm) = %{tl_version}, tex(bkaimp15.tfm) = %{tl_version}
Provides:       tex(bkaimp16.tfm) = %{tl_version}, tex(bkaimp17.tfm) = %{tl_version}
Provides:       tex(bkaimp18.tfm) = %{tl_version}, tex(bkaimp19.tfm) = %{tl_version}
Provides:       tex(bkaimp20.tfm) = %{tl_version}, tex(bkaimp21.tfm) = %{tl_version}
Provides:       tex(bkaimp22.tfm) = %{tl_version}, tex(bkaimp23.tfm) = %{tl_version}
Provides:       tex(bkaimp25.tfm) = %{tl_version}, tex(bkaimp26.tfm) = %{tl_version}
Provides:       tex(bkaimp27.tfm) = %{tl_version}, tex(bkaimp28.tfm) = %{tl_version}
Provides:       tex(bkaimp29.tfm) = %{tl_version}, tex(bkaimp30.tfm) = %{tl_version}
Provides:       tex(bkaimp31.tfm) = %{tl_version}, tex(bkaimp32.tfm) = %{tl_version}
Provides:       tex(bkaimp33.tfm) = %{tl_version}, tex(bkaimp34.tfm) = %{tl_version}
Provides:       tex(bkaimp35.tfm) = %{tl_version}, tex(bkaimp36.tfm) = %{tl_version}
Provides:       tex(bkaimp37.tfm) = %{tl_version}, tex(bkaimp38.tfm) = %{tl_version}
Provides:       tex(bkaimp39.tfm) = %{tl_version}, tex(bkaimp40.tfm) = %{tl_version}
Provides:       tex(bkaimp41.tfm) = %{tl_version}, tex(bkaimp42.tfm) = %{tl_version}
Provides:       tex(bkaimp43.tfm) = %{tl_version}, tex(bkaimp44.tfm) = %{tl_version}
Provides:       tex(bkaimp45.tfm) = %{tl_version}, tex(bkaimp46.tfm) = %{tl_version}
Provides:       tex(bkaimp47.tfm) = %{tl_version}, tex(bkaimp48.tfm) = %{tl_version}
Provides:       tex(bkaimp49.tfm) = %{tl_version}, tex(bkaimp50.tfm) = %{tl_version}
Provides:       tex(bkaimp51.tfm) = %{tl_version}, tex(bkaimp52.tfm) = %{tl_version}
Provides:       tex(bkaimp53.tfm) = %{tl_version}, tex(bkaimp54.tfm) = %{tl_version}
Provides:       tex(bkaimp55.tfm) = %{tl_version}, tex(bkaimpv.tfm) = %{tl_version}
Provides:       tex(bkaiu00.tfm) = %{tl_version}, tex(bkaiu02.tfm) = %{tl_version}
Provides:       tex(bkaiu03.tfm) = %{tl_version}, tex(bkaiu20.tfm) = %{tl_version}
Provides:       tex(bkaiu21.tfm) = %{tl_version}, tex(bkaiu22.tfm) = %{tl_version}
Provides:       tex(bkaiu25.tfm) = %{tl_version}, tex(bkaiu26.tfm) = %{tl_version}
Provides:       tex(bkaiu30.tfm) = %{tl_version}, tex(bkaiu31.tfm) = %{tl_version}
Provides:       tex(bkaiu32.tfm) = %{tl_version}, tex(bkaiu33.tfm) = %{tl_version}
Provides:       tex(bkaiu4e.tfm) = %{tl_version}, tex(bkaiu4f.tfm) = %{tl_version}
Provides:       tex(bkaiu50.tfm) = %{tl_version}, tex(bkaiu51.tfm) = %{tl_version}
Provides:       tex(bkaiu52.tfm) = %{tl_version}, tex(bkaiu53.tfm) = %{tl_version}
Provides:       tex(bkaiu54.tfm) = %{tl_version}, tex(bkaiu55.tfm) = %{tl_version}
Provides:       tex(bkaiu56.tfm) = %{tl_version}, tex(bkaiu57.tfm) = %{tl_version}
Provides:       tex(bkaiu58.tfm) = %{tl_version}, tex(bkaiu59.tfm) = %{tl_version}
Provides:       tex(bkaiu5a.tfm) = %{tl_version}, tex(bkaiu5b.tfm) = %{tl_version}
Provides:       tex(bkaiu5c.tfm) = %{tl_version}, tex(bkaiu5d.tfm) = %{tl_version}
Provides:       tex(bkaiu5e.tfm) = %{tl_version}, tex(bkaiu5f.tfm) = %{tl_version}
Provides:       tex(bkaiu60.tfm) = %{tl_version}, tex(bkaiu61.tfm) = %{tl_version}
Provides:       tex(bkaiu62.tfm) = %{tl_version}, tex(bkaiu63.tfm) = %{tl_version}
Provides:       tex(bkaiu64.tfm) = %{tl_version}, tex(bkaiu65.tfm) = %{tl_version}
Provides:       tex(bkaiu66.tfm) = %{tl_version}, tex(bkaiu67.tfm) = %{tl_version}
Provides:       tex(bkaiu68.tfm) = %{tl_version}, tex(bkaiu69.tfm) = %{tl_version}
Provides:       tex(bkaiu6a.tfm) = %{tl_version}, tex(bkaiu6b.tfm) = %{tl_version}
Provides:       tex(bkaiu6c.tfm) = %{tl_version}, tex(bkaiu6d.tfm) = %{tl_version}
Provides:       tex(bkaiu6e.tfm) = %{tl_version}, tex(bkaiu6f.tfm) = %{tl_version}
Provides:       tex(bkaiu70.tfm) = %{tl_version}, tex(bkaiu71.tfm) = %{tl_version}
Provides:       tex(bkaiu72.tfm) = %{tl_version}, tex(bkaiu73.tfm) = %{tl_version}
Provides:       tex(bkaiu74.tfm) = %{tl_version}, tex(bkaiu75.tfm) = %{tl_version}
Provides:       tex(bkaiu76.tfm) = %{tl_version}, tex(bkaiu77.tfm) = %{tl_version}
Provides:       tex(bkaiu78.tfm) = %{tl_version}, tex(bkaiu79.tfm) = %{tl_version}
Provides:       tex(bkaiu7a.tfm) = %{tl_version}, tex(bkaiu7b.tfm) = %{tl_version}
Provides:       tex(bkaiu7c.tfm) = %{tl_version}, tex(bkaiu7d.tfm) = %{tl_version}
Provides:       tex(bkaiu7e.tfm) = %{tl_version}, tex(bkaiu7f.tfm) = %{tl_version}
Provides:       tex(bkaiu80.tfm) = %{tl_version}, tex(bkaiu81.tfm) = %{tl_version}
Provides:       tex(bkaiu82.tfm) = %{tl_version}, tex(bkaiu83.tfm) = %{tl_version}
Provides:       tex(bkaiu84.tfm) = %{tl_version}, tex(bkaiu85.tfm) = %{tl_version}
Provides:       tex(bkaiu86.tfm) = %{tl_version}, tex(bkaiu87.tfm) = %{tl_version}
Provides:       tex(bkaiu88.tfm) = %{tl_version}, tex(bkaiu89.tfm) = %{tl_version}
Provides:       tex(bkaiu8a.tfm) = %{tl_version}, tex(bkaiu8b.tfm) = %{tl_version}
Provides:       tex(bkaiu8c.tfm) = %{tl_version}, tex(bkaiu8d.tfm) = %{tl_version}
Provides:       tex(bkaiu8e.tfm) = %{tl_version}, tex(bkaiu8f.tfm) = %{tl_version}
Provides:       tex(bkaiu90.tfm) = %{tl_version}, tex(bkaiu91.tfm) = %{tl_version}
Provides:       tex(bkaiu92.tfm) = %{tl_version}, tex(bkaiu93.tfm) = %{tl_version}
Provides:       tex(bkaiu94.tfm) = %{tl_version}, tex(bkaiu95.tfm) = %{tl_version}
Provides:       tex(bkaiu96.tfm) = %{tl_version}, tex(bkaiu97.tfm) = %{tl_version}
Provides:       tex(bkaiu98.tfm) = %{tl_version}, tex(bkaiu99.tfm) = %{tl_version}
Provides:       tex(bkaiu9a.tfm) = %{tl_version}, tex(bkaiu9b.tfm) = %{tl_version}
Provides:       tex(bkaiu9c.tfm) = %{tl_version}, tex(bkaiu9d.tfm) = %{tl_version}
Provides:       tex(bkaiu9e.tfm) = %{tl_version}, tex(bkaiu9f.tfm) = %{tl_version}
Provides:       tex(bkaiuee.tfm) = %{tl_version}, tex(bkaiuf6.tfm) = %{tl_version}
Provides:       tex(bkaiuf7.tfm) = %{tl_version}, tex(bkaiuf8.tfm) = %{tl_version}
Provides:       tex(bkaiufa.tfm) = %{tl_version}, tex(bkaiufe.tfm) = %{tl_version}
Provides:       tex(bkaiuff.tfm) = %{tl_version}, tex(bkaiuv.tfm) = %{tl_version}
Provides:       tex(bsmilp00.tfm) = %{tl_version}, tex(bsmilp01.tfm) = %{tl_version}
Provides:       tex(bsmilp02.tfm) = %{tl_version}, tex(bsmilp03.tfm) = %{tl_version}
Provides:       tex(bsmilp04.tfm) = %{tl_version}, tex(bsmilp05.tfm) = %{tl_version}
Provides:       tex(bsmilp06.tfm) = %{tl_version}, tex(bsmilp07.tfm) = %{tl_version}
Provides:       tex(bsmilp08.tfm) = %{tl_version}, tex(bsmilp09.tfm) = %{tl_version}
Provides:       tex(bsmilp10.tfm) = %{tl_version}, tex(bsmilp11.tfm) = %{tl_version}
Provides:       tex(bsmilp12.tfm) = %{tl_version}, tex(bsmilp13.tfm) = %{tl_version}
Provides:       tex(bsmilp14.tfm) = %{tl_version}, tex(bsmilp15.tfm) = %{tl_version}
Provides:       tex(bsmilp16.tfm) = %{tl_version}, tex(bsmilp17.tfm) = %{tl_version}
Provides:       tex(bsmilp18.tfm) = %{tl_version}, tex(bsmilp19.tfm) = %{tl_version}
Provides:       tex(bsmilp20.tfm) = %{tl_version}, tex(bsmilp21.tfm) = %{tl_version}
Provides:       tex(bsmilp22.tfm) = %{tl_version}, tex(bsmilp23.tfm) = %{tl_version}
Provides:       tex(bsmilp25.tfm) = %{tl_version}, tex(bsmilp26.tfm) = %{tl_version}
Provides:       tex(bsmilp27.tfm) = %{tl_version}, tex(bsmilp28.tfm) = %{tl_version}
Provides:       tex(bsmilp29.tfm) = %{tl_version}, tex(bsmilp30.tfm) = %{tl_version}
Provides:       tex(bsmilp31.tfm) = %{tl_version}, tex(bsmilp32.tfm) = %{tl_version}
Provides:       tex(bsmilp33.tfm) = %{tl_version}, tex(bsmilp34.tfm) = %{tl_version}
Provides:       tex(bsmilp35.tfm) = %{tl_version}, tex(bsmilp36.tfm) = %{tl_version}
Provides:       tex(bsmilp37.tfm) = %{tl_version}, tex(bsmilp38.tfm) = %{tl_version}
Provides:       tex(bsmilp39.tfm) = %{tl_version}, tex(bsmilp40.tfm) = %{tl_version}
Provides:       tex(bsmilp41.tfm) = %{tl_version}, tex(bsmilp42.tfm) = %{tl_version}
Provides:       tex(bsmilp43.tfm) = %{tl_version}, tex(bsmilp44.tfm) = %{tl_version}
Provides:       tex(bsmilp45.tfm) = %{tl_version}, tex(bsmilp46.tfm) = %{tl_version}
Provides:       tex(bsmilp47.tfm) = %{tl_version}, tex(bsmilp48.tfm) = %{tl_version}
Provides:       tex(bsmilp49.tfm) = %{tl_version}, tex(bsmilp50.tfm) = %{tl_version}
Provides:       tex(bsmilp51.tfm) = %{tl_version}, tex(bsmilp52.tfm) = %{tl_version}
Provides:       tex(bsmilp53.tfm) = %{tl_version}, tex(bsmilp54.tfm) = %{tl_version}
Provides:       tex(bsmilp55.tfm) = %{tl_version}, tex(bsmilpv.tfm) = %{tl_version}
Provides:       tex(bsmiu00.tfm) = %{tl_version}, tex(bsmiu02.tfm) = %{tl_version}
Provides:       tex(bsmiu03.tfm) = %{tl_version}, tex(bsmiu20.tfm) = %{tl_version}
Provides:       tex(bsmiu21.tfm) = %{tl_version}, tex(bsmiu22.tfm) = %{tl_version}
Provides:       tex(bsmiu25.tfm) = %{tl_version}, tex(bsmiu26.tfm) = %{tl_version}
Provides:       tex(bsmiu30.tfm) = %{tl_version}, tex(bsmiu31.tfm) = %{tl_version}
Provides:       tex(bsmiu32.tfm) = %{tl_version}, tex(bsmiu33.tfm) = %{tl_version}
Provides:       tex(bsmiu4e.tfm) = %{tl_version}, tex(bsmiu4f.tfm) = %{tl_version}
Provides:       tex(bsmiu50.tfm) = %{tl_version}, tex(bsmiu51.tfm) = %{tl_version}
Provides:       tex(bsmiu52.tfm) = %{tl_version}, tex(bsmiu53.tfm) = %{tl_version}
Provides:       tex(bsmiu54.tfm) = %{tl_version}, tex(bsmiu55.tfm) = %{tl_version}
Provides:       tex(bsmiu56.tfm) = %{tl_version}, tex(bsmiu57.tfm) = %{tl_version}
Provides:       tex(bsmiu58.tfm) = %{tl_version}, tex(bsmiu59.tfm) = %{tl_version}
Provides:       tex(bsmiu5a.tfm) = %{tl_version}, tex(bsmiu5b.tfm) = %{tl_version}
Provides:       tex(bsmiu5c.tfm) = %{tl_version}, tex(bsmiu5d.tfm) = %{tl_version}
Provides:       tex(bsmiu5e.tfm) = %{tl_version}, tex(bsmiu5f.tfm) = %{tl_version}
Provides:       tex(bsmiu60.tfm) = %{tl_version}, tex(bsmiu61.tfm) = %{tl_version}
Provides:       tex(bsmiu62.tfm) = %{tl_version}, tex(bsmiu63.tfm) = %{tl_version}
Provides:       tex(bsmiu64.tfm) = %{tl_version}, tex(bsmiu65.tfm) = %{tl_version}
Provides:       tex(bsmiu66.tfm) = %{tl_version}, tex(bsmiu67.tfm) = %{tl_version}
Provides:       tex(bsmiu68.tfm) = %{tl_version}, tex(bsmiu69.tfm) = %{tl_version}
Provides:       tex(bsmiu6a.tfm) = %{tl_version}, tex(bsmiu6b.tfm) = %{tl_version}
Provides:       tex(bsmiu6c.tfm) = %{tl_version}, tex(bsmiu6d.tfm) = %{tl_version}
Provides:       tex(bsmiu6e.tfm) = %{tl_version}, tex(bsmiu6f.tfm) = %{tl_version}
Provides:       tex(bsmiu70.tfm) = %{tl_version}, tex(bsmiu71.tfm) = %{tl_version}
Provides:       tex(bsmiu72.tfm) = %{tl_version}, tex(bsmiu73.tfm) = %{tl_version}
Provides:       tex(bsmiu74.tfm) = %{tl_version}, tex(bsmiu75.tfm) = %{tl_version}
Provides:       tex(bsmiu76.tfm) = %{tl_version}, tex(bsmiu77.tfm) = %{tl_version}
Provides:       tex(bsmiu78.tfm) = %{tl_version}, tex(bsmiu79.tfm) = %{tl_version}
Provides:       tex(bsmiu7a.tfm) = %{tl_version}, tex(bsmiu7b.tfm) = %{tl_version}
Provides:       tex(bsmiu7c.tfm) = %{tl_version}, tex(bsmiu7d.tfm) = %{tl_version}
Provides:       tex(bsmiu7e.tfm) = %{tl_version}, tex(bsmiu7f.tfm) = %{tl_version}
Provides:       tex(bsmiu80.tfm) = %{tl_version}, tex(bsmiu81.tfm) = %{tl_version}
Provides:       tex(bsmiu82.tfm) = %{tl_version}, tex(bsmiu83.tfm) = %{tl_version}
Provides:       tex(bsmiu84.tfm) = %{tl_version}, tex(bsmiu85.tfm) = %{tl_version}
Provides:       tex(bsmiu86.tfm) = %{tl_version}, tex(bsmiu87.tfm) = %{tl_version}
Provides:       tex(bsmiu88.tfm) = %{tl_version}, tex(bsmiu89.tfm) = %{tl_version}
Provides:       tex(bsmiu8a.tfm) = %{tl_version}, tex(bsmiu8b.tfm) = %{tl_version}
Provides:       tex(bsmiu8c.tfm) = %{tl_version}, tex(bsmiu8d.tfm) = %{tl_version}
Provides:       tex(bsmiu8e.tfm) = %{tl_version}, tex(bsmiu8f.tfm) = %{tl_version}
Provides:       tex(bsmiu90.tfm) = %{tl_version}, tex(bsmiu91.tfm) = %{tl_version}
Provides:       tex(bsmiu92.tfm) = %{tl_version}, tex(bsmiu93.tfm) = %{tl_version}
Provides:       tex(bsmiu94.tfm) = %{tl_version}, tex(bsmiu95.tfm) = %{tl_version}
Provides:       tex(bsmiu96.tfm) = %{tl_version}, tex(bsmiu97.tfm) = %{tl_version}
Provides:       tex(bsmiu98.tfm) = %{tl_version}, tex(bsmiu99.tfm) = %{tl_version}
Provides:       tex(bsmiu9a.tfm) = %{tl_version}, tex(bsmiu9b.tfm) = %{tl_version}
Provides:       tex(bsmiu9c.tfm) = %{tl_version}, tex(bsmiu9d.tfm) = %{tl_version}
Provides:       tex(bsmiu9e.tfm) = %{tl_version}, tex(bsmiu9f.tfm) = %{tl_version}
Provides:       tex(bsmiuee.tfm) = %{tl_version}, tex(bsmiuf6.tfm) = %{tl_version}
Provides:       tex(bsmiuf7.tfm) = %{tl_version}, tex(bsmiuf8.tfm) = %{tl_version}
Provides:       tex(bsmiufa.tfm) = %{tl_version}, tex(bsmiufe.tfm) = %{tl_version}
Provides:       tex(bsmiuff.tfm) = %{tl_version}, tex(bsmiuv.tfm) = %{tl_version}
Provides:       tex(gbsnlp00.tfm) = %{tl_version}, tex(gbsnlp01.tfm) = %{tl_version}
Provides:       tex(gbsnlp02.tfm) = %{tl_version}, tex(gbsnlp03.tfm) = %{tl_version}
Provides:       tex(gbsnlp04.tfm) = %{tl_version}, tex(gbsnlp06.tfm) = %{tl_version}
Provides:       tex(gbsnlp07.tfm) = %{tl_version}, tex(gbsnlp08.tfm) = %{tl_version}
Provides:       tex(gbsnlp09.tfm) = %{tl_version}, tex(gbsnlp10.tfm) = %{tl_version}
Provides:       tex(gbsnlp11.tfm) = %{tl_version}, tex(gbsnlp12.tfm) = %{tl_version}
Provides:       tex(gbsnlp13.tfm) = %{tl_version}, tex(gbsnlp14.tfm) = %{tl_version}
Provides:       tex(gbsnlp15.tfm) = %{tl_version}, tex(gbsnlp16.tfm) = %{tl_version}
Provides:       tex(gbsnlp17.tfm) = %{tl_version}, tex(gbsnlp18.tfm) = %{tl_version}
Provides:       tex(gbsnlp19.tfm) = %{tl_version}, tex(gbsnlp20.tfm) = %{tl_version}
Provides:       tex(gbsnlp21.tfm) = %{tl_version}, tex(gbsnlp22.tfm) = %{tl_version}
Provides:       tex(gbsnlp23.tfm) = %{tl_version}, tex(gbsnlp24.tfm) = %{tl_version}
Provides:       tex(gbsnlp25.tfm) = %{tl_version}, tex(gbsnlp26.tfm) = %{tl_version}
Provides:       tex(gbsnlp27.tfm) = %{tl_version}, tex(gbsnlp28.tfm) = %{tl_version}
Provides:       tex(gbsnlp29.tfm) = %{tl_version}, tex(gbsnlp30.tfm) = %{tl_version}
Provides:       tex(gbsnlp31.tfm) = %{tl_version}, tex(gbsnlp32.tfm) = %{tl_version}
Provides:       tex(gbsnu00.tfm) = %{tl_version}, tex(gbsnu01.tfm) = %{tl_version}
Provides:       tex(gbsnu02.tfm) = %{tl_version}, tex(gbsnu03.tfm) = %{tl_version}
Provides:       tex(gbsnu04.tfm) = %{tl_version}, tex(gbsnu20.tfm) = %{tl_version}
Provides:       tex(gbsnu21.tfm) = %{tl_version}, tex(gbsnu22.tfm) = %{tl_version}
Provides:       tex(gbsnu23.tfm) = %{tl_version}, tex(gbsnu24.tfm) = %{tl_version}
Provides:       tex(gbsnu25.tfm) = %{tl_version}, tex(gbsnu26.tfm) = %{tl_version}
Provides:       tex(gbsnu30.tfm) = %{tl_version}, tex(gbsnu31.tfm) = %{tl_version}
Provides:       tex(gbsnu32.tfm) = %{tl_version}, tex(gbsnu4e.tfm) = %{tl_version}
Provides:       tex(gbsnu4f.tfm) = %{tl_version}, tex(gbsnu50.tfm) = %{tl_version}
Provides:       tex(gbsnu51.tfm) = %{tl_version}, tex(gbsnu52.tfm) = %{tl_version}
Provides:       tex(gbsnu53.tfm) = %{tl_version}, tex(gbsnu54.tfm) = %{tl_version}
Provides:       tex(gbsnu55.tfm) = %{tl_version}, tex(gbsnu56.tfm) = %{tl_version}
Provides:       tex(gbsnu57.tfm) = %{tl_version}, tex(gbsnu58.tfm) = %{tl_version}
Provides:       tex(gbsnu59.tfm) = %{tl_version}, tex(gbsnu5a.tfm) = %{tl_version}
Provides:       tex(gbsnu5b.tfm) = %{tl_version}, tex(gbsnu5c.tfm) = %{tl_version}
Provides:       tex(gbsnu5d.tfm) = %{tl_version}, tex(gbsnu5e.tfm) = %{tl_version}
Provides:       tex(gbsnu5f.tfm) = %{tl_version}, tex(gbsnu60.tfm) = %{tl_version}
Provides:       tex(gbsnu61.tfm) = %{tl_version}, tex(gbsnu62.tfm) = %{tl_version}
Provides:       tex(gbsnu63.tfm) = %{tl_version}, tex(gbsnu64.tfm) = %{tl_version}
Provides:       tex(gbsnu65.tfm) = %{tl_version}, tex(gbsnu66.tfm) = %{tl_version}
Provides:       tex(gbsnu67.tfm) = %{tl_version}, tex(gbsnu68.tfm) = %{tl_version}
Provides:       tex(gbsnu69.tfm) = %{tl_version}, tex(gbsnu6a.tfm) = %{tl_version}
Provides:       tex(gbsnu6b.tfm) = %{tl_version}, tex(gbsnu6c.tfm) = %{tl_version}
Provides:       tex(gbsnu6d.tfm) = %{tl_version}, tex(gbsnu6e.tfm) = %{tl_version}
Provides:       tex(gbsnu6f.tfm) = %{tl_version}, tex(gbsnu70.tfm) = %{tl_version}
Provides:       tex(gbsnu71.tfm) = %{tl_version}, tex(gbsnu72.tfm) = %{tl_version}
Provides:       tex(gbsnu73.tfm) = %{tl_version}, tex(gbsnu74.tfm) = %{tl_version}
Provides:       tex(gbsnu75.tfm) = %{tl_version}, tex(gbsnu76.tfm) = %{tl_version}
Provides:       tex(gbsnu77.tfm) = %{tl_version}, tex(gbsnu78.tfm) = %{tl_version}
Provides:       tex(gbsnu79.tfm) = %{tl_version}, tex(gbsnu7a.tfm) = %{tl_version}
Provides:       tex(gbsnu7b.tfm) = %{tl_version}, tex(gbsnu7c.tfm) = %{tl_version}
Provides:       tex(gbsnu7d.tfm) = %{tl_version}, tex(gbsnu7e.tfm) = %{tl_version}
Provides:       tex(gbsnu7f.tfm) = %{tl_version}, tex(gbsnu80.tfm) = %{tl_version}
Provides:       tex(gbsnu81.tfm) = %{tl_version}, tex(gbsnu82.tfm) = %{tl_version}
Provides:       tex(gbsnu83.tfm) = %{tl_version}, tex(gbsnu84.tfm) = %{tl_version}
Provides:       tex(gbsnu85.tfm) = %{tl_version}, tex(gbsnu86.tfm) = %{tl_version}
Provides:       tex(gbsnu87.tfm) = %{tl_version}, tex(gbsnu88.tfm) = %{tl_version}
Provides:       tex(gbsnu89.tfm) = %{tl_version}, tex(gbsnu8a.tfm) = %{tl_version}
Provides:       tex(gbsnu8b.tfm) = %{tl_version}, tex(gbsnu8c.tfm) = %{tl_version}
Provides:       tex(gbsnu8d.tfm) = %{tl_version}, tex(gbsnu8e.tfm) = %{tl_version}
Provides:       tex(gbsnu8f.tfm) = %{tl_version}, tex(gbsnu90.tfm) = %{tl_version}
Provides:       tex(gbsnu91.tfm) = %{tl_version}, tex(gbsnu92.tfm) = %{tl_version}
Provides:       tex(gbsnu93.tfm) = %{tl_version}, tex(gbsnu94.tfm) = %{tl_version}
Provides:       tex(gbsnu95.tfm) = %{tl_version}, tex(gbsnu96.tfm) = %{tl_version}
Provides:       tex(gbsnu97.tfm) = %{tl_version}, tex(gbsnu98.tfm) = %{tl_version}
Provides:       tex(gbsnu99.tfm) = %{tl_version}, tex(gbsnu9a.tfm) = %{tl_version}
Provides:       tex(gbsnu9b.tfm) = %{tl_version}, tex(gbsnu9c.tfm) = %{tl_version}
Provides:       tex(gbsnu9e.tfm) = %{tl_version}, tex(gbsnu9f.tfm) = %{tl_version}
Provides:       tex(gbsnufe.tfm) = %{tl_version}, tex(gbsnuff.tfm) = %{tl_version}
Provides:       tex(gkaimp00.tfm) = %{tl_version}, tex(gkaimp01.tfm) = %{tl_version}
Provides:       tex(gkaimp02.tfm) = %{tl_version}, tex(gkaimp03.tfm) = %{tl_version}
Provides:       tex(gkaimp04.tfm) = %{tl_version}, tex(gkaimp06.tfm) = %{tl_version}
Provides:       tex(gkaimp07.tfm) = %{tl_version}, tex(gkaimp08.tfm) = %{tl_version}
Provides:       tex(gkaimp09.tfm) = %{tl_version}, tex(gkaimp10.tfm) = %{tl_version}
Provides:       tex(gkaimp11.tfm) = %{tl_version}, tex(gkaimp12.tfm) = %{tl_version}
Provides:       tex(gkaimp13.tfm) = %{tl_version}, tex(gkaimp14.tfm) = %{tl_version}
Provides:       tex(gkaimp15.tfm) = %{tl_version}, tex(gkaimp16.tfm) = %{tl_version}
Provides:       tex(gkaimp17.tfm) = %{tl_version}, tex(gkaimp18.tfm) = %{tl_version}
Provides:       tex(gkaimp19.tfm) = %{tl_version}, tex(gkaimp20.tfm) = %{tl_version}
Provides:       tex(gkaimp21.tfm) = %{tl_version}, tex(gkaimp22.tfm) = %{tl_version}
Provides:       tex(gkaimp23.tfm) = %{tl_version}, tex(gkaimp24.tfm) = %{tl_version}
Provides:       tex(gkaimp25.tfm) = %{tl_version}, tex(gkaimp26.tfm) = %{tl_version}
Provides:       tex(gkaimp27.tfm) = %{tl_version}, tex(gkaimp28.tfm) = %{tl_version}
Provides:       tex(gkaimp29.tfm) = %{tl_version}, tex(gkaimp30.tfm) = %{tl_version}
Provides:       tex(gkaimp31.tfm) = %{tl_version}, tex(gkaimp32.tfm) = %{tl_version}
Provides:       tex(gkaiu00.tfm) = %{tl_version}, tex(gkaiu01.tfm) = %{tl_version}
Provides:       tex(gkaiu02.tfm) = %{tl_version}, tex(gkaiu03.tfm) = %{tl_version}
Provides:       tex(gkaiu04.tfm) = %{tl_version}, tex(gkaiu20.tfm) = %{tl_version}
Provides:       tex(gkaiu21.tfm) = %{tl_version}, tex(gkaiu22.tfm) = %{tl_version}
Provides:       tex(gkaiu23.tfm) = %{tl_version}, tex(gkaiu24.tfm) = %{tl_version}
Provides:       tex(gkaiu25.tfm) = %{tl_version}, tex(gkaiu26.tfm) = %{tl_version}
Provides:       tex(gkaiu30.tfm) = %{tl_version}, tex(gkaiu31.tfm) = %{tl_version}
Provides:       tex(gkaiu32.tfm) = %{tl_version}, tex(gkaiu4e.tfm) = %{tl_version}
Provides:       tex(gkaiu4f.tfm) = %{tl_version}, tex(gkaiu50.tfm) = %{tl_version}
Provides:       tex(gkaiu51.tfm) = %{tl_version}, tex(gkaiu52.tfm) = %{tl_version}
Provides:       tex(gkaiu53.tfm) = %{tl_version}, tex(gkaiu54.tfm) = %{tl_version}
Provides:       tex(gkaiu55.tfm) = %{tl_version}, tex(gkaiu56.tfm) = %{tl_version}
Provides:       tex(gkaiu57.tfm) = %{tl_version}, tex(gkaiu58.tfm) = %{tl_version}
Provides:       tex(gkaiu59.tfm) = %{tl_version}, tex(gkaiu5a.tfm) = %{tl_version}
Provides:       tex(gkaiu5b.tfm) = %{tl_version}, tex(gkaiu5c.tfm) = %{tl_version}
Provides:       tex(gkaiu5d.tfm) = %{tl_version}, tex(gkaiu5e.tfm) = %{tl_version}
Provides:       tex(gkaiu5f.tfm) = %{tl_version}, tex(gkaiu60.tfm) = %{tl_version}
Provides:       tex(gkaiu61.tfm) = %{tl_version}, tex(gkaiu62.tfm) = %{tl_version}
Provides:       tex(gkaiu63.tfm) = %{tl_version}, tex(gkaiu64.tfm) = %{tl_version}
Provides:       tex(gkaiu65.tfm) = %{tl_version}, tex(gkaiu66.tfm) = %{tl_version}
Provides:       tex(gkaiu67.tfm) = %{tl_version}, tex(gkaiu68.tfm) = %{tl_version}
Provides:       tex(gkaiu69.tfm) = %{tl_version}, tex(gkaiu6a.tfm) = %{tl_version}
Provides:       tex(gkaiu6b.tfm) = %{tl_version}, tex(gkaiu6c.tfm) = %{tl_version}
Provides:       tex(gkaiu6d.tfm) = %{tl_version}, tex(gkaiu6e.tfm) = %{tl_version}
Provides:       tex(gkaiu6f.tfm) = %{tl_version}, tex(gkaiu70.tfm) = %{tl_version}
Provides:       tex(gkaiu71.tfm) = %{tl_version}, tex(gkaiu72.tfm) = %{tl_version}
Provides:       tex(gkaiu73.tfm) = %{tl_version}, tex(gkaiu74.tfm) = %{tl_version}
Provides:       tex(gkaiu75.tfm) = %{tl_version}, tex(gkaiu76.tfm) = %{tl_version}
Provides:       tex(gkaiu77.tfm) = %{tl_version}, tex(gkaiu78.tfm) = %{tl_version}
Provides:       tex(gkaiu79.tfm) = %{tl_version}, tex(gkaiu7a.tfm) = %{tl_version}
Provides:       tex(gkaiu7b.tfm) = %{tl_version}, tex(gkaiu7c.tfm) = %{tl_version}
Provides:       tex(gkaiu7d.tfm) = %{tl_version}, tex(gkaiu7e.tfm) = %{tl_version}
Provides:       tex(gkaiu7f.tfm) = %{tl_version}, tex(gkaiu80.tfm) = %{tl_version}
Provides:       tex(gkaiu81.tfm) = %{tl_version}, tex(gkaiu82.tfm) = %{tl_version}
Provides:       tex(gkaiu83.tfm) = %{tl_version}, tex(gkaiu84.tfm) = %{tl_version}
Provides:       tex(gkaiu85.tfm) = %{tl_version}, tex(gkaiu86.tfm) = %{tl_version}
Provides:       tex(gkaiu87.tfm) = %{tl_version}, tex(gkaiu88.tfm) = %{tl_version}
Provides:       tex(gkaiu89.tfm) = %{tl_version}, tex(gkaiu8a.tfm) = %{tl_version}
Provides:       tex(gkaiu8b.tfm) = %{tl_version}, tex(gkaiu8c.tfm) = %{tl_version}
Provides:       tex(gkaiu8d.tfm) = %{tl_version}, tex(gkaiu8e.tfm) = %{tl_version}
Provides:       tex(gkaiu8f.tfm) = %{tl_version}, tex(gkaiu90.tfm) = %{tl_version}
Provides:       tex(gkaiu91.tfm) = %{tl_version}, tex(gkaiu92.tfm) = %{tl_version}
Provides:       tex(gkaiu93.tfm) = %{tl_version}, tex(gkaiu94.tfm) = %{tl_version}
Provides:       tex(gkaiu95.tfm) = %{tl_version}, tex(gkaiu96.tfm) = %{tl_version}
Provides:       tex(gkaiu97.tfm) = %{tl_version}, tex(gkaiu98.tfm) = %{tl_version}
Provides:       tex(gkaiu99.tfm) = %{tl_version}, tex(gkaiu9a.tfm) = %{tl_version}
Provides:       tex(gkaiu9b.tfm) = %{tl_version}, tex(gkaiu9c.tfm) = %{tl_version}
Provides:       tex(gkaiu9e.tfm) = %{tl_version}, tex(gkaiu9f.tfm) = %{tl_version}
Provides:       tex(gkaiufe.tfm) = %{tl_version}, tex(gkaiuff.tfm) = %{tl_version}
Provides:       tex(bkaiu00.pfb) = %{tl_version}, tex(bkaiu02.pfb) = %{tl_version}
Provides:       tex(bkaiu03.pfb) = %{tl_version}, tex(bkaiu20.pfb) = %{tl_version}
Provides:       tex(bkaiu21.pfb) = %{tl_version}, tex(bkaiu22.pfb) = %{tl_version}
Provides:       tex(bkaiu25.pfb) = %{tl_version}, tex(bkaiu26.pfb) = %{tl_version}
Provides:       tex(bkaiu30.pfb) = %{tl_version}, tex(bkaiu31.pfb) = %{tl_version}
Provides:       tex(bkaiu32.pfb) = %{tl_version}, tex(bkaiu33.pfb) = %{tl_version}
Provides:       tex(bkaiu4e.pfb) = %{tl_version}, tex(bkaiu4f.pfb) = %{tl_version}
Provides:       tex(bkaiu50.pfb) = %{tl_version}, tex(bkaiu51.pfb) = %{tl_version}
Provides:       tex(bkaiu52.pfb) = %{tl_version}, tex(bkaiu53.pfb) = %{tl_version}
Provides:       tex(bkaiu54.pfb) = %{tl_version}, tex(bkaiu55.pfb) = %{tl_version}
Provides:       tex(bkaiu56.pfb) = %{tl_version}, tex(bkaiu57.pfb) = %{tl_version}
Provides:       tex(bkaiu58.pfb) = %{tl_version}, tex(bkaiu59.pfb) = %{tl_version}
Provides:       tex(bkaiu5a.pfb) = %{tl_version}, tex(bkaiu5b.pfb) = %{tl_version}
Provides:       tex(bkaiu5c.pfb) = %{tl_version}, tex(bkaiu5d.pfb) = %{tl_version}
Provides:       tex(bkaiu5e.pfb) = %{tl_version}, tex(bkaiu5f.pfb) = %{tl_version}
Provides:       tex(bkaiu60.pfb) = %{tl_version}, tex(bkaiu61.pfb) = %{tl_version}
Provides:       tex(bkaiu62.pfb) = %{tl_version}, tex(bkaiu63.pfb) = %{tl_version}
Provides:       tex(bkaiu64.pfb) = %{tl_version}, tex(bkaiu65.pfb) = %{tl_version}
Provides:       tex(bkaiu66.pfb) = %{tl_version}, tex(bkaiu67.pfb) = %{tl_version}
Provides:       tex(bkaiu68.pfb) = %{tl_version}, tex(bkaiu69.pfb) = %{tl_version}
Provides:       tex(bkaiu6a.pfb) = %{tl_version}, tex(bkaiu6b.pfb) = %{tl_version}
Provides:       tex(bkaiu6c.pfb) = %{tl_version}, tex(bkaiu6d.pfb) = %{tl_version}
Provides:       tex(bkaiu6e.pfb) = %{tl_version}, tex(bkaiu6f.pfb) = %{tl_version}
Provides:       tex(bkaiu70.pfb) = %{tl_version}, tex(bkaiu71.pfb) = %{tl_version}
Provides:       tex(bkaiu72.pfb) = %{tl_version}, tex(bkaiu73.pfb) = %{tl_version}
Provides:       tex(bkaiu74.pfb) = %{tl_version}, tex(bkaiu75.pfb) = %{tl_version}
Provides:       tex(bkaiu76.pfb) = %{tl_version}, tex(bkaiu77.pfb) = %{tl_version}
Provides:       tex(bkaiu78.pfb) = %{tl_version}, tex(bkaiu79.pfb) = %{tl_version}
Provides:       tex(bkaiu7a.pfb) = %{tl_version}, tex(bkaiu7b.pfb) = %{tl_version}
Provides:       tex(bkaiu7c.pfb) = %{tl_version}, tex(bkaiu7d.pfb) = %{tl_version}
Provides:       tex(bkaiu7e.pfb) = %{tl_version}, tex(bkaiu7f.pfb) = %{tl_version}
Provides:       tex(bkaiu80.pfb) = %{tl_version}, tex(bkaiu81.pfb) = %{tl_version}
Provides:       tex(bkaiu82.pfb) = %{tl_version}, tex(bkaiu83.pfb) = %{tl_version}
Provides:       tex(bkaiu84.pfb) = %{tl_version}, tex(bkaiu85.pfb) = %{tl_version}
Provides:       tex(bkaiu86.pfb) = %{tl_version}, tex(bkaiu87.pfb) = %{tl_version}
Provides:       tex(bkaiu88.pfb) = %{tl_version}, tex(bkaiu89.pfb) = %{tl_version}
Provides:       tex(bkaiu8a.pfb) = %{tl_version}, tex(bkaiu8b.pfb) = %{tl_version}
Provides:       tex(bkaiu8c.pfb) = %{tl_version}, tex(bkaiu8d.pfb) = %{tl_version}
Provides:       tex(bkaiu8e.pfb) = %{tl_version}, tex(bkaiu8f.pfb) = %{tl_version}
Provides:       tex(bkaiu90.pfb) = %{tl_version}, tex(bkaiu91.pfb) = %{tl_version}
Provides:       tex(bkaiu92.pfb) = %{tl_version}, tex(bkaiu93.pfb) = %{tl_version}
Provides:       tex(bkaiu94.pfb) = %{tl_version}, tex(bkaiu95.pfb) = %{tl_version}
Provides:       tex(bkaiu96.pfb) = %{tl_version}, tex(bkaiu97.pfb) = %{tl_version}
Provides:       tex(bkaiu98.pfb) = %{tl_version}, tex(bkaiu99.pfb) = %{tl_version}
Provides:       tex(bkaiu9a.pfb) = %{tl_version}, tex(bkaiu9b.pfb) = %{tl_version}
Provides:       tex(bkaiu9c.pfb) = %{tl_version}, tex(bkaiu9d.pfb) = %{tl_version}
Provides:       tex(bkaiu9e.pfb) = %{tl_version}, tex(bkaiu9f.pfb) = %{tl_version}
Provides:       tex(bkaiuee.pfb) = %{tl_version}, tex(bkaiuf6.pfb) = %{tl_version}
Provides:       tex(bkaiuf7.pfb) = %{tl_version}, tex(bkaiuf8.pfb) = %{tl_version}
Provides:       tex(bkaiufa.pfb) = %{tl_version}, tex(bkaiufe.pfb) = %{tl_version}
Provides:       tex(bkaiuff.pfb) = %{tl_version}, tex(bkaiuv.pfb) = %{tl_version}
Provides:       tex(bsmiu00.pfb) = %{tl_version}, tex(bsmiu02.pfb) = %{tl_version}
Provides:       tex(bsmiu03.pfb) = %{tl_version}, tex(bsmiu20.pfb) = %{tl_version}
Provides:       tex(bsmiu21.pfb) = %{tl_version}, tex(bsmiu22.pfb) = %{tl_version}
Provides:       tex(bsmiu25.pfb) = %{tl_version}, tex(bsmiu26.pfb) = %{tl_version}
Provides:       tex(bsmiu30.pfb) = %{tl_version}, tex(bsmiu31.pfb) = %{tl_version}
Provides:       tex(bsmiu32.pfb) = %{tl_version}, tex(bsmiu33.pfb) = %{tl_version}
Provides:       tex(bsmiu4e.pfb) = %{tl_version}, tex(bsmiu4f.pfb) = %{tl_version}
Provides:       tex(bsmiu50.pfb) = %{tl_version}, tex(bsmiu51.pfb) = %{tl_version}
Provides:       tex(bsmiu52.pfb) = %{tl_version}, tex(bsmiu53.pfb) = %{tl_version}
Provides:       tex(bsmiu54.pfb) = %{tl_version}, tex(bsmiu55.pfb) = %{tl_version}
Provides:       tex(bsmiu56.pfb) = %{tl_version}, tex(bsmiu57.pfb) = %{tl_version}
Provides:       tex(bsmiu58.pfb) = %{tl_version}, tex(bsmiu59.pfb) = %{tl_version}
Provides:       tex(bsmiu5a.pfb) = %{tl_version}, tex(bsmiu5b.pfb) = %{tl_version}
Provides:       tex(bsmiu5c.pfb) = %{tl_version}, tex(bsmiu5d.pfb) = %{tl_version}
Provides:       tex(bsmiu5e.pfb) = %{tl_version}, tex(bsmiu5f.pfb) = %{tl_version}
Provides:       tex(bsmiu60.pfb) = %{tl_version}, tex(bsmiu61.pfb) = %{tl_version}
Provides:       tex(bsmiu62.pfb) = %{tl_version}, tex(bsmiu63.pfb) = %{tl_version}
Provides:       tex(bsmiu64.pfb) = %{tl_version}, tex(bsmiu65.pfb) = %{tl_version}
Provides:       tex(bsmiu66.pfb) = %{tl_version}, tex(bsmiu67.pfb) = %{tl_version}
Provides:       tex(bsmiu68.pfb) = %{tl_version}, tex(bsmiu69.pfb) = %{tl_version}
Provides:       tex(bsmiu6a.pfb) = %{tl_version}, tex(bsmiu6b.pfb) = %{tl_version}
Provides:       tex(bsmiu6c.pfb) = %{tl_version}, tex(bsmiu6d.pfb) = %{tl_version}
Provides:       tex(bsmiu6e.pfb) = %{tl_version}, tex(bsmiu6f.pfb) = %{tl_version}
Provides:       tex(bsmiu70.pfb) = %{tl_version}, tex(bsmiu71.pfb) = %{tl_version}
Provides:       tex(bsmiu72.pfb) = %{tl_version}, tex(bsmiu73.pfb) = %{tl_version}
Provides:       tex(bsmiu74.pfb) = %{tl_version}, tex(bsmiu75.pfb) = %{tl_version}
Provides:       tex(bsmiu76.pfb) = %{tl_version}, tex(bsmiu77.pfb) = %{tl_version}
Provides:       tex(bsmiu78.pfb) = %{tl_version}, tex(bsmiu79.pfb) = %{tl_version}
Provides:       tex(bsmiu7a.pfb) = %{tl_version}, tex(bsmiu7b.pfb) = %{tl_version}
Provides:       tex(bsmiu7c.pfb) = %{tl_version}, tex(bsmiu7d.pfb) = %{tl_version}
Provides:       tex(bsmiu7e.pfb) = %{tl_version}, tex(bsmiu7f.pfb) = %{tl_version}
Provides:       tex(bsmiu80.pfb) = %{tl_version}, tex(bsmiu81.pfb) = %{tl_version}
Provides:       tex(bsmiu82.pfb) = %{tl_version}, tex(bsmiu83.pfb) = %{tl_version}
Provides:       tex(bsmiu84.pfb) = %{tl_version}, tex(bsmiu85.pfb) = %{tl_version}
Provides:       tex(bsmiu86.pfb) = %{tl_version}, tex(bsmiu87.pfb) = %{tl_version}
Provides:       tex(bsmiu88.pfb) = %{tl_version}, tex(bsmiu89.pfb) = %{tl_version}
Provides:       tex(bsmiu8a.pfb) = %{tl_version}, tex(bsmiu8b.pfb) = %{tl_version}
Provides:       tex(bsmiu8c.pfb) = %{tl_version}, tex(bsmiu8d.pfb) = %{tl_version}
Provides:       tex(bsmiu8e.pfb) = %{tl_version}, tex(bsmiu8f.pfb) = %{tl_version}
Provides:       tex(bsmiu90.pfb) = %{tl_version}, tex(bsmiu91.pfb) = %{tl_version}
Provides:       tex(bsmiu92.pfb) = %{tl_version}, tex(bsmiu93.pfb) = %{tl_version}
Provides:       tex(bsmiu94.pfb) = %{tl_version}, tex(bsmiu95.pfb) = %{tl_version}
Provides:       tex(bsmiu96.pfb) = %{tl_version}, tex(bsmiu97.pfb) = %{tl_version}
Provides:       tex(bsmiu98.pfb) = %{tl_version}, tex(bsmiu99.pfb) = %{tl_version}
Provides:       tex(bsmiu9a.pfb) = %{tl_version}, tex(bsmiu9b.pfb) = %{tl_version}
Provides:       tex(bsmiu9c.pfb) = %{tl_version}, tex(bsmiu9d.pfb) = %{tl_version}
Provides:       tex(bsmiu9e.pfb) = %{tl_version}, tex(bsmiu9f.pfb) = %{tl_version}
Provides:       tex(bsmiuee.pfb) = %{tl_version}, tex(bsmiuf6.pfb) = %{tl_version}
Provides:       tex(bsmiuf7.pfb) = %{tl_version}, tex(bsmiuf8.pfb) = %{tl_version}
Provides:       tex(bsmiufa.pfb) = %{tl_version}, tex(bsmiufe.pfb) = %{tl_version}
Provides:       tex(bsmiuff.pfb) = %{tl_version}, tex(bsmiuv.pfb) = %{tl_version}
Provides:       tex(gbsnu00.pfb) = %{tl_version}, tex(gbsnu01.pfb) = %{tl_version}
Provides:       tex(gbsnu02.pfb) = %{tl_version}, tex(gbsnu03.pfb) = %{tl_version}
Provides:       tex(gbsnu04.pfb) = %{tl_version}, tex(gbsnu20.pfb) = %{tl_version}
Provides:       tex(gbsnu21.pfb) = %{tl_version}, tex(gbsnu22.pfb) = %{tl_version}
Provides:       tex(gbsnu23.pfb) = %{tl_version}, tex(gbsnu24.pfb) = %{tl_version}
Provides:       tex(gbsnu25.pfb) = %{tl_version}, tex(gbsnu26.pfb) = %{tl_version}
Provides:       tex(gbsnu30.pfb) = %{tl_version}, tex(gbsnu31.pfb) = %{tl_version}
Provides:       tex(gbsnu32.pfb) = %{tl_version}, tex(gbsnu4e.pfb) = %{tl_version}
Provides:       tex(gbsnu4f.pfb) = %{tl_version}, tex(gbsnu50.pfb) = %{tl_version}
Provides:       tex(gbsnu51.pfb) = %{tl_version}, tex(gbsnu52.pfb) = %{tl_version}
Provides:       tex(gbsnu53.pfb) = %{tl_version}, tex(gbsnu54.pfb) = %{tl_version}
Provides:       tex(gbsnu55.pfb) = %{tl_version}, tex(gbsnu56.pfb) = %{tl_version}
Provides:       tex(gbsnu57.pfb) = %{tl_version}, tex(gbsnu58.pfb) = %{tl_version}
Provides:       tex(gbsnu59.pfb) = %{tl_version}, tex(gbsnu5a.pfb) = %{tl_version}
Provides:       tex(gbsnu5b.pfb) = %{tl_version}, tex(gbsnu5c.pfb) = %{tl_version}
Provides:       tex(gbsnu5d.pfb) = %{tl_version}, tex(gbsnu5e.pfb) = %{tl_version}
Provides:       tex(gbsnu5f.pfb) = %{tl_version}, tex(gbsnu60.pfb) = %{tl_version}
Provides:       tex(gbsnu61.pfb) = %{tl_version}, tex(gbsnu62.pfb) = %{tl_version}
Provides:       tex(gbsnu63.pfb) = %{tl_version}, tex(gbsnu64.pfb) = %{tl_version}
Provides:       tex(gbsnu65.pfb) = %{tl_version}, tex(gbsnu66.pfb) = %{tl_version}
Provides:       tex(gbsnu67.pfb) = %{tl_version}, tex(gbsnu68.pfb) = %{tl_version}
Provides:       tex(gbsnu69.pfb) = %{tl_version}, tex(gbsnu6a.pfb) = %{tl_version}
Provides:       tex(gbsnu6b.pfb) = %{tl_version}, tex(gbsnu6c.pfb) = %{tl_version}
Provides:       tex(gbsnu6d.pfb) = %{tl_version}, tex(gbsnu6e.pfb) = %{tl_version}
Provides:       tex(gbsnu6f.pfb) = %{tl_version}, tex(gbsnu70.pfb) = %{tl_version}
Provides:       tex(gbsnu71.pfb) = %{tl_version}, tex(gbsnu72.pfb) = %{tl_version}
Provides:       tex(gbsnu73.pfb) = %{tl_version}, tex(gbsnu74.pfb) = %{tl_version}
Provides:       tex(gbsnu75.pfb) = %{tl_version}, tex(gbsnu76.pfb) = %{tl_version}
Provides:       tex(gbsnu77.pfb) = %{tl_version}, tex(gbsnu78.pfb) = %{tl_version}
Provides:       tex(gbsnu79.pfb) = %{tl_version}, tex(gbsnu7a.pfb) = %{tl_version}
Provides:       tex(gbsnu7b.pfb) = %{tl_version}, tex(gbsnu7c.pfb) = %{tl_version}
Provides:       tex(gbsnu7d.pfb) = %{tl_version}, tex(gbsnu7e.pfb) = %{tl_version}
Provides:       tex(gbsnu7f.pfb) = %{tl_version}, tex(gbsnu80.pfb) = %{tl_version}
Provides:       tex(gbsnu81.pfb) = %{tl_version}, tex(gbsnu82.pfb) = %{tl_version}
Provides:       tex(gbsnu83.pfb) = %{tl_version}, tex(gbsnu84.pfb) = %{tl_version}
Provides:       tex(gbsnu85.pfb) = %{tl_version}, tex(gbsnu86.pfb) = %{tl_version}
Provides:       tex(gbsnu87.pfb) = %{tl_version}, tex(gbsnu88.pfb) = %{tl_version}
Provides:       tex(gbsnu89.pfb) = %{tl_version}, tex(gbsnu8a.pfb) = %{tl_version}
Provides:       tex(gbsnu8b.pfb) = %{tl_version}, tex(gbsnu8c.pfb) = %{tl_version}
Provides:       tex(gbsnu8d.pfb) = %{tl_version}, tex(gbsnu8e.pfb) = %{tl_version}
Provides:       tex(gbsnu8f.pfb) = %{tl_version}, tex(gbsnu90.pfb) = %{tl_version}
Provides:       tex(gbsnu91.pfb) = %{tl_version}, tex(gbsnu92.pfb) = %{tl_version}
Provides:       tex(gbsnu93.pfb) = %{tl_version}, tex(gbsnu94.pfb) = %{tl_version}
Provides:       tex(gbsnu95.pfb) = %{tl_version}, tex(gbsnu96.pfb) = %{tl_version}
Provides:       tex(gbsnu97.pfb) = %{tl_version}, tex(gbsnu98.pfb) = %{tl_version}
Provides:       tex(gbsnu99.pfb) = %{tl_version}, tex(gbsnu9a.pfb) = %{tl_version}
Provides:       tex(gbsnu9b.pfb) = %{tl_version}, tex(gbsnu9c.pfb) = %{tl_version}
Provides:       tex(gbsnu9e.pfb) = %{tl_version}, tex(gbsnu9f.pfb) = %{tl_version}
Provides:       tex(gbsnufe.pfb) = %{tl_version}, tex(gbsnuff.pfb) = %{tl_version}
Provides:       tex(gkaiu00.pfb) = %{tl_version}, tex(gkaiu01.pfb) = %{tl_version}
Provides:       tex(gkaiu02.pfb) = %{tl_version}, tex(gkaiu03.pfb) = %{tl_version}
Provides:       tex(gkaiu04.pfb) = %{tl_version}, tex(gkaiu20.pfb) = %{tl_version}
Provides:       tex(gkaiu21.pfb) = %{tl_version}, tex(gkaiu22.pfb) = %{tl_version}
Provides:       tex(gkaiu23.pfb) = %{tl_version}, tex(gkaiu24.pfb) = %{tl_version}
Provides:       tex(gkaiu25.pfb) = %{tl_version}, tex(gkaiu26.pfb) = %{tl_version}
Provides:       tex(gkaiu30.pfb) = %{tl_version}, tex(gkaiu31.pfb) = %{tl_version}
Provides:       tex(gkaiu32.pfb) = %{tl_version}, tex(gkaiu4e.pfb) = %{tl_version}
Provides:       tex(gkaiu4f.pfb) = %{tl_version}, tex(gkaiu50.pfb) = %{tl_version}
Provides:       tex(gkaiu51.pfb) = %{tl_version}, tex(gkaiu52.pfb) = %{tl_version}
Provides:       tex(gkaiu53.pfb) = %{tl_version}, tex(gkaiu54.pfb) = %{tl_version}
Provides:       tex(gkaiu55.pfb) = %{tl_version}, tex(gkaiu56.pfb) = %{tl_version}
Provides:       tex(gkaiu57.pfb) = %{tl_version}, tex(gkaiu58.pfb) = %{tl_version}
Provides:       tex(gkaiu59.pfb) = %{tl_version}, tex(gkaiu5a.pfb) = %{tl_version}
Provides:       tex(gkaiu5b.pfb) = %{tl_version}, tex(gkaiu5c.pfb) = %{tl_version}
Provides:       tex(gkaiu5d.pfb) = %{tl_version}, tex(gkaiu5e.pfb) = %{tl_version}
Provides:       tex(gkaiu5f.pfb) = %{tl_version}, tex(gkaiu60.pfb) = %{tl_version}
Provides:       tex(gkaiu61.pfb) = %{tl_version}, tex(gkaiu62.pfb) = %{tl_version}
Provides:       tex(gkaiu63.pfb) = %{tl_version}, tex(gkaiu64.pfb) = %{tl_version}
Provides:       tex(gkaiu65.pfb) = %{tl_version}, tex(gkaiu66.pfb) = %{tl_version}
Provides:       tex(gkaiu67.pfb) = %{tl_version}, tex(gkaiu68.pfb) = %{tl_version}
Provides:       tex(gkaiu69.pfb) = %{tl_version}, tex(gkaiu6a.pfb) = %{tl_version}
Provides:       tex(gkaiu6b.pfb) = %{tl_version}, tex(gkaiu6c.pfb) = %{tl_version}
Provides:       tex(gkaiu6d.pfb) = %{tl_version}, tex(gkaiu6e.pfb) = %{tl_version}
Provides:       tex(gkaiu6f.pfb) = %{tl_version}, tex(gkaiu70.pfb) = %{tl_version}
Provides:       tex(gkaiu71.pfb) = %{tl_version}, tex(gkaiu72.pfb) = %{tl_version}
Provides:       tex(gkaiu73.pfb) = %{tl_version}, tex(gkaiu74.pfb) = %{tl_version}
Provides:       tex(gkaiu75.pfb) = %{tl_version}, tex(gkaiu76.pfb) = %{tl_version}
Provides:       tex(gkaiu77.pfb) = %{tl_version}, tex(gkaiu78.pfb) = %{tl_version}
Provides:       tex(gkaiu79.pfb) = %{tl_version}, tex(gkaiu7a.pfb) = %{tl_version}
Provides:       tex(gkaiu7b.pfb) = %{tl_version}, tex(gkaiu7c.pfb) = %{tl_version}
Provides:       tex(gkaiu7d.pfb) = %{tl_version}, tex(gkaiu7e.pfb) = %{tl_version}
Provides:       tex(gkaiu7f.pfb) = %{tl_version}, tex(gkaiu80.pfb) = %{tl_version}
Provides:       tex(gkaiu81.pfb) = %{tl_version}, tex(gkaiu82.pfb) = %{tl_version}
Provides:       tex(gkaiu83.pfb) = %{tl_version}, tex(gkaiu84.pfb) = %{tl_version}
Provides:       tex(gkaiu85.pfb) = %{tl_version}, tex(gkaiu86.pfb) = %{tl_version}
Provides:       tex(gkaiu87.pfb) = %{tl_version}, tex(gkaiu88.pfb) = %{tl_version}
Provides:       tex(gkaiu89.pfb) = %{tl_version}, tex(gkaiu8a.pfb) = %{tl_version}
Provides:       tex(gkaiu8b.pfb) = %{tl_version}, tex(gkaiu8c.pfb) = %{tl_version}
Provides:       tex(gkaiu8d.pfb) = %{tl_version}, tex(gkaiu8e.pfb) = %{tl_version}
Provides:       tex(gkaiu8f.pfb) = %{tl_version}, tex(gkaiu90.pfb) = %{tl_version}
Provides:       tex(gkaiu91.pfb) = %{tl_version}, tex(gkaiu92.pfb) = %{tl_version}
Provides:       tex(gkaiu93.pfb) = %{tl_version}, tex(gkaiu94.pfb) = %{tl_version}
Provides:       tex(gkaiu95.pfb) = %{tl_version}, tex(gkaiu96.pfb) = %{tl_version}
Provides:       tex(gkaiu97.pfb) = %{tl_version}, tex(gkaiu98.pfb) = %{tl_version}
Provides:       tex(gkaiu99.pfb) = %{tl_version}, tex(gkaiu9a.pfb) = %{tl_version}
Provides:       tex(gkaiu9b.pfb) = %{tl_version}, tex(gkaiu9c.pfb) = %{tl_version}
Provides:       tex(gkaiu9e.pfb) = %{tl_version}, tex(gkaiu9f.pfb) = %{tl_version}
Provides:       tex(gkaiufe.pfb) = %{tl_version}, tex(gkaiuff.pfb) = %{tl_version}
Provides:       tex(bkaimp00.vf) = %{tl_version}, tex(bkaimp01.vf) = %{tl_version}
Provides:       tex(bkaimp02.vf) = %{tl_version}, tex(bkaimp03.vf) = %{tl_version}
Provides:       tex(bkaimp04.vf) = %{tl_version}, tex(bkaimp05.vf) = %{tl_version}
Provides:       tex(bkaimp06.vf) = %{tl_version}, tex(bkaimp07.vf) = %{tl_version}
Provides:       tex(bkaimp08.vf) = %{tl_version}, tex(bkaimp09.vf) = %{tl_version}
Provides:       tex(bkaimp10.vf) = %{tl_version}, tex(bkaimp11.vf) = %{tl_version}
Provides:       tex(bkaimp12.vf) = %{tl_version}, tex(bkaimp13.vf) = %{tl_version}
Provides:       tex(bkaimp14.vf) = %{tl_version}, tex(bkaimp15.vf) = %{tl_version}
Provides:       tex(bkaimp16.vf) = %{tl_version}, tex(bkaimp17.vf) = %{tl_version}
Provides:       tex(bkaimp18.vf) = %{tl_version}, tex(bkaimp19.vf) = %{tl_version}
Provides:       tex(bkaimp20.vf) = %{tl_version}, tex(bkaimp21.vf) = %{tl_version}
Provides:       tex(bkaimp22.vf) = %{tl_version}, tex(bkaimp23.vf) = %{tl_version}
Provides:       tex(bkaimp25.vf) = %{tl_version}, tex(bkaimp26.vf) = %{tl_version}
Provides:       tex(bkaimp27.vf) = %{tl_version}, tex(bkaimp28.vf) = %{tl_version}
Provides:       tex(bkaimp29.vf) = %{tl_version}, tex(bkaimp30.vf) = %{tl_version}
Provides:       tex(bkaimp31.vf) = %{tl_version}, tex(bkaimp32.vf) = %{tl_version}
Provides:       tex(bkaimp33.vf) = %{tl_version}, tex(bkaimp34.vf) = %{tl_version}
Provides:       tex(bkaimp35.vf) = %{tl_version}, tex(bkaimp36.vf) = %{tl_version}
Provides:       tex(bkaimp37.vf) = %{tl_version}, tex(bkaimp38.vf) = %{tl_version}
Provides:       tex(bkaimp39.vf) = %{tl_version}, tex(bkaimp40.vf) = %{tl_version}
Provides:       tex(bkaimp41.vf) = %{tl_version}, tex(bkaimp42.vf) = %{tl_version}
Provides:       tex(bkaimp43.vf) = %{tl_version}, tex(bkaimp44.vf) = %{tl_version}
Provides:       tex(bkaimp45.vf) = %{tl_version}, tex(bkaimp46.vf) = %{tl_version}
Provides:       tex(bkaimp47.vf) = %{tl_version}, tex(bkaimp48.vf) = %{tl_version}
Provides:       tex(bkaimp49.vf) = %{tl_version}, tex(bkaimp50.vf) = %{tl_version}
Provides:       tex(bkaimp51.vf) = %{tl_version}, tex(bkaimp52.vf) = %{tl_version}
Provides:       tex(bkaimp53.vf) = %{tl_version}, tex(bkaimp54.vf) = %{tl_version}
Provides:       tex(bkaimp55.vf) = %{tl_version}, tex(bkaimpv.vf) = %{tl_version}
Provides:       tex(bsmilp00.vf) = %{tl_version}, tex(bsmilp01.vf) = %{tl_version}
Provides:       tex(bsmilp02.vf) = %{tl_version}, tex(bsmilp03.vf) = %{tl_version}
Provides:       tex(bsmilp04.vf) = %{tl_version}, tex(bsmilp05.vf) = %{tl_version}
Provides:       tex(bsmilp06.vf) = %{tl_version}, tex(bsmilp07.vf) = %{tl_version}
Provides:       tex(bsmilp08.vf) = %{tl_version}, tex(bsmilp09.vf) = %{tl_version}
Provides:       tex(bsmilp10.vf) = %{tl_version}, tex(bsmilp11.vf) = %{tl_version}
Provides:       tex(bsmilp12.vf) = %{tl_version}, tex(bsmilp13.vf) = %{tl_version}
Provides:       tex(bsmilp14.vf) = %{tl_version}, tex(bsmilp15.vf) = %{tl_version}
Provides:       tex(bsmilp16.vf) = %{tl_version}, tex(bsmilp17.vf) = %{tl_version}
Provides:       tex(bsmilp18.vf) = %{tl_version}, tex(bsmilp19.vf) = %{tl_version}
Provides:       tex(bsmilp20.vf) = %{tl_version}, tex(bsmilp21.vf) = %{tl_version}
Provides:       tex(bsmilp22.vf) = %{tl_version}, tex(bsmilp23.vf) = %{tl_version}
Provides:       tex(bsmilp25.vf) = %{tl_version}, tex(bsmilp26.vf) = %{tl_version}
Provides:       tex(bsmilp27.vf) = %{tl_version}, tex(bsmilp28.vf) = %{tl_version}
Provides:       tex(bsmilp29.vf) = %{tl_version}, tex(bsmilp30.vf) = %{tl_version}
Provides:       tex(bsmilp31.vf) = %{tl_version}, tex(bsmilp32.vf) = %{tl_version}
Provides:       tex(bsmilp33.vf) = %{tl_version}, tex(bsmilp34.vf) = %{tl_version}
Provides:       tex(bsmilp35.vf) = %{tl_version}, tex(bsmilp36.vf) = %{tl_version}
Provides:       tex(bsmilp37.vf) = %{tl_version}, tex(bsmilp38.vf) = %{tl_version}
Provides:       tex(bsmilp39.vf) = %{tl_version}, tex(bsmilp40.vf) = %{tl_version}
Provides:       tex(bsmilp41.vf) = %{tl_version}, tex(bsmilp42.vf) = %{tl_version}
Provides:       tex(bsmilp43.vf) = %{tl_version}, tex(bsmilp44.vf) = %{tl_version}
Provides:       tex(bsmilp45.vf) = %{tl_version}, tex(bsmilp46.vf) = %{tl_version}
Provides:       tex(bsmilp47.vf) = %{tl_version}, tex(bsmilp48.vf) = %{tl_version}
Provides:       tex(bsmilp49.vf) = %{tl_version}, tex(bsmilp50.vf) = %{tl_version}
Provides:       tex(bsmilp51.vf) = %{tl_version}, tex(bsmilp52.vf) = %{tl_version}
Provides:       tex(bsmilp53.vf) = %{tl_version}, tex(bsmilp54.vf) = %{tl_version}
Provides:       tex(bsmilp55.vf) = %{tl_version}, tex(bsmilpv.vf) = %{tl_version}
Provides:       tex(gbsnlp00.vf) = %{tl_version}, tex(gbsnlp01.vf) = %{tl_version}
Provides:       tex(gbsnlp02.vf) = %{tl_version}, tex(gbsnlp03.vf) = %{tl_version}
Provides:       tex(gbsnlp04.vf) = %{tl_version}, tex(gbsnlp06.vf) = %{tl_version}
Provides:       tex(gbsnlp07.vf) = %{tl_version}, tex(gbsnlp08.vf) = %{tl_version}
Provides:       tex(gbsnlp09.vf) = %{tl_version}, tex(gbsnlp10.vf) = %{tl_version}
Provides:       tex(gbsnlp11.vf) = %{tl_version}, tex(gbsnlp12.vf) = %{tl_version}
Provides:       tex(gbsnlp13.vf) = %{tl_version}, tex(gbsnlp14.vf) = %{tl_version}
Provides:       tex(gbsnlp15.vf) = %{tl_version}, tex(gbsnlp16.vf) = %{tl_version}
Provides:       tex(gbsnlp17.vf) = %{tl_version}, tex(gbsnlp18.vf) = %{tl_version}
Provides:       tex(gbsnlp19.vf) = %{tl_version}, tex(gbsnlp20.vf) = %{tl_version}
Provides:       tex(gbsnlp21.vf) = %{tl_version}, tex(gbsnlp22.vf) = %{tl_version}
Provides:       tex(gbsnlp23.vf) = %{tl_version}, tex(gbsnlp24.vf) = %{tl_version}
Provides:       tex(gbsnlp25.vf) = %{tl_version}, tex(gbsnlp26.vf) = %{tl_version}
Provides:       tex(gbsnlp27.vf) = %{tl_version}, tex(gbsnlp28.vf) = %{tl_version}
Provides:       tex(gbsnlp29.vf) = %{tl_version}, tex(gbsnlp30.vf) = %{tl_version}
Provides:       tex(gbsnlp31.vf) = %{tl_version}, tex(gbsnlp32.vf) = %{tl_version}
Provides:       tex(gkaimp00.vf) = %{tl_version}, tex(gkaimp01.vf) = %{tl_version}
Provides:       tex(gkaimp02.vf) = %{tl_version}, tex(gkaimp03.vf) = %{tl_version}
Provides:       tex(gkaimp04.vf) = %{tl_version}, tex(gkaimp06.vf) = %{tl_version}
Provides:       tex(gkaimp07.vf) = %{tl_version}, tex(gkaimp08.vf) = %{tl_version}
Provides:       tex(gkaimp09.vf) = %{tl_version}, tex(gkaimp10.vf) = %{tl_version}
Provides:       tex(gkaimp11.vf) = %{tl_version}, tex(gkaimp12.vf) = %{tl_version}
Provides:       tex(gkaimp13.vf) = %{tl_version}, tex(gkaimp14.vf) = %{tl_version}
Provides:       tex(gkaimp15.vf) = %{tl_version}, tex(gkaimp16.vf) = %{tl_version}
Provides:       tex(gkaimp17.vf) = %{tl_version}, tex(gkaimp18.vf) = %{tl_version}
Provides:       tex(gkaimp19.vf) = %{tl_version}, tex(gkaimp20.vf) = %{tl_version}
Provides:       tex(gkaimp21.vf) = %{tl_version}, tex(gkaimp22.vf) = %{tl_version}
Provides:       tex(gkaimp23.vf) = %{tl_version}, tex(gkaimp24.vf) = %{tl_version}
Provides:       tex(gkaimp25.vf) = %{tl_version}, tex(gkaimp26.vf) = %{tl_version}
Provides:       tex(gkaimp27.vf) = %{tl_version}, tex(gkaimp28.vf) = %{tl_version}
Provides:       tex(gkaimp29.vf) = %{tl_version}, tex(gkaimp30.vf) = %{tl_version}
Provides:       tex(gkaimp31.vf) = %{tl_version}, tex(gkaimp32.vf) = %{tl_version}

%description -n texlive-arphic
These are font bundles for the Chinese Arphic fonts which work
with the CJK package. Arphic is actually the name of the
company that which created the fonts (and put them under a GPL-
like licence).

%package -n texlive-arphic-doc
Summary:        Documentation for arphic
Version:        svn15878.0

Provides:       tex-arphic-doc
AutoReqProv:    No

%description -n texlive-arphic-doc
Documentation for arphic

%package -n texlive-arrayjobx
Provides:       tex-arrayjobx = %{tl_version}
License:        LPPL
Summary:        Array data structures for (La)TeX
Version:        svn18125.1.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(arrayjob.sty) = %{tl_version}, tex(arrayjobx.sty) = %{tl_version}

%description -n texlive-arrayjobx
This package provides array data structures in (La)TeX, in the
meaning of the classical procedural programming languages like
Fortran, Ada or C, and macros to manipulate them. Arrays can be
mono or bi-dimensional. This is useful for applications which
require high level programming techniques, like algorithmic
graphics programmed in the TeX language. The package supersedes
the arrayjob package.

%package -n texlive-arrayjobx-doc
Summary:        Documentation for arrayjobx
Version:        svn18125.1.04

Provides:       tex-arrayjobx-doc
AutoReqProv:    No

%description -n texlive-arrayjobx-doc
Documentation for arrayjobx

%package -n texlive-arraysort
Provides:       tex-arraysort = %{tl_version}
License:        LPPL 1.2
Summary:        Sort arrays (or portions of them)
Version:        svn31576.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pdftexcmds.sty), tex(lcg.sty), tex(arrayjobx.sty), tex(calc.sty)
Requires:       tex(ifthen.sty), tex(etoolbox.sty), tex(xargs.sty), tex(macroswap.sty)
Provides:       tex(arraysort.sty) = %{tl_version}

%description -n texlive-arraysort
The package provides a mechanism for sorting arrays (or
portions of them); the arrays should have been created using
the arrayjobx package.

%package -n texlive-arraysort-doc
Summary:        Documentation for arraysort
Version:        svn31576.1.0

Provides:       tex-arraysort-doc
AutoReqProv:    No

%description -n texlive-arraysort-doc
Documentation for arraysort

%package -n texlive-arsclassica
Provides:       tex-arsclassica = %{tl_version}
License:        LPPL
Summary:        A different view of the ClassicThesis package
Version:        svn45656
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(classicthesis.sty), tex(caption.sty)
Requires:       tex(soul.sty), tex(titlesec.sty)
Provides:       tex(arsclassica.sty) = %{tl_version}

%description -n texlive-arsclassica
The package changes some typographical points of the
ClassicThesis style, by Andre Miede. It enables the user to
reproduce the look of the guide The art of writing with LaTeX
(the web page is in Italian).

%package -n texlive-arsclassica-doc
Summary:        Documentation for arsclassica
Version:        svn45656
Provides:       tex-arsclassica-doc
AutoReqProv:    No

%description -n texlive-arsclassica-doc
Documentation for arsclassica

%package -n texlive-articleingud
Provides:       tex-articleingud = %{tl_version}
License:        LPPL 1.2
Summary:        LaTeX class for articles published in INGENIERIA review
Version:        svn38741

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(articleingud.cls) = %{tl_version}

%description -n texlive-articleingud
The class is for articles published in INGENIERIA review. It is
derived from the standard LaTeX class article.

%package -n texlive-articleingud-doc
Summary:        Documentation for articleingud
Version:        svn38741

Provides:       tex-articleingud-doc
AutoReqProv:    No

%description -n texlive-articleingud-doc
Documentation for articleingud

%package -n texlive-arydshln
Provides:       tex-arydshln = %{tl_version}
License:        LPPL
Summary:        Horizontal and vertical dashed lines in arrays and tabulars
Version:        svn40847
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(arydshln.sty) = %{tl_version}

%description -n texlive-arydshln
Definitions of horizontal and vertical dashed lines for the
array and tabular environment. Horizontal lines are drawn by
\hdashline and \cdashline while vertical ones can be specified
as a part of preamble using ':'. The shape of dashed lines may
be controlled through style parameters or optional arguments.
The package is compatible with array and colortab.

%package -n texlive-arydshln-doc
Summary:        Documentation for arydshln
Version:        svn40847
Provides:       tex-arydshln-doc
AutoReqProv:    No

%description -n texlive-arydshln-doc
Documentation for arydshln

%package -n texlive-asaetr
Provides:       tex-asaetr = %{tl_version}
License:        Public Domain
Summary:        Transactions of the ASAE
Version:        svn15878.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(asaesub.sty) = %{tl_version}, tex(asaetr.cls) = %{tl_version}
Provides:       tex(asaetr.sty) = %{tl_version}

%description -n texlive-asaetr
A class and BibTeX style for submissions to the Transactions of
the American Society of Agricultural Engineers. Also included
is the Metafont source of a slanted Computer Modern Caps and
Small Caps font.

%package -n texlive-asaetr-doc
Summary:        Documentation for asaetr
Version:        svn15878.1.0a

Provides:       tex-asaetr-doc
AutoReqProv:    No

%description -n texlive-asaetr-doc
Documentation for asaetr

%package asana-math
Provides:       tex-asana-math = %{tl_version}
License:        OFL
Summary:        A font to typeset maths in Xe(La)TeX and Lua(La)TeX
Version:        svn37556.000.955

Requires:       texlive-base
Provides:       texlive-Asana-Math = %{tl_version}
Obsoletes:      texlive-Asana-Math < %{tl_version}, texlive-Asana-Math-fedora-fonts < %{tl_version}
Requires:       texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Asana-Math.otf) = %{tl_version}

%description asana-math
The Asana-Math font is an OpenType font that includes almost
all mathematical Unicode symbols and it can be used to typeset
mathematical text with any software that can understand the
MATH OpenType table (e.g., XeTeX 0.997 and Microsoft Word
2007). The font is beta software. Typesetting support for use
with LaTeX is provided by the fontspec and unicode-math
packages.

%package asana-math-doc
Summary:        Documentation for asana-math
Version:        svn37556.000.955

Provides:       tex-asana-math-doc
AutoReqProv:    No

%description asana-math-doc
Documentation for asana-math

%package -n texlive-ascelike
Provides:       tex-ascelike = %{tl_version}
License:        LPPL
Summary:        Bibliography style for the ASCE
Version:        svn29129.2.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(endfloat.sty), tex(setspace.sty), tex(lineno.sty)
Provides:       tex(ascelike.cls) = %{tl_version}

%description -n texlive-ascelike
A document class and bibliographic style that prepares
documents in the style required by the American Society of
Civil Engineers (ASCE). These are unofficial files, not
sanctioned by that organization, and the files specifically
give this caveat. Also included is a short
documentation/example of how to use the class.

%package -n texlive-ascelike-doc
Summary:        Documentation for ascelike
Version:        svn29129.2.3

Provides:       tex-ascelike-doc
AutoReqProv:    No

%description -n texlive-ascelike-doc
Documentation for ascelike

%package -n texlive-ascii-chart-doc
Summary:        Documentation for ascii-chart
Version:        svn20536.0

Provides:       tex-ascii-chart-doc
AutoReqProv:    No

%description -n texlive-ascii-chart-doc
Documentation for ascii-chart

%package -n texlive-ascii-font
Provides:       tex-ascii-font = %{tl_version}
License:        LPPL
Summary:        Use the ASCII "font" in LaTeX
Version:        svn29989.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xspace.sty)
Provides:       tex(ascii.map) = %{tl_version}, tex(ASCII.tfm) = %{tl_version}
Provides:       tex(ASCII.pfb) = %{tl_version}, tex(ascii.sty) = %{tl_version}

%description -n texlive-ascii-font
The package provides glyph and font access commands so that
LaTeX users can use the ASCII glyphs in their documents. The
ASCII font is encoded according to the IBM PC Code Page 437 C0
Graphics. This package replaces any early LaTeX 2.09 package
and "font" by R. Ramasubramanian and R.W.D. Nickalls.

%package -n texlive-ascii-font-doc
Summary:        Documentation for ascii-font
Version:        svn29989.2.0

Provides:       tex-ascii-font-doc
AutoReqProv:    No

%description -n texlive-ascii-font-doc
Documentation for ascii-font

%package -n texlive-askmaps
Provides:       tex-askmaps = %{tl_version}
License:        LPPL
Summary:        Typeset American style Karnaugh maps
Version:        svn32320.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pict2e.sty)
Provides:       tex(askmaps.sty) = %{tl_version}

%description -n texlive-askmaps
The package provides 2, 3, 4 and 5 variable Karnaugh maps, in
the style used in numerous textbooks on digital design. The
package draws K-maps where the most significant input variables
are placed on top of the columns and the least significant
variables are placed left of the rows.

%package -n texlive-askmaps-doc
Summary:        Documentation for askmaps
Version:        svn32320.0.1

Provides:       tex-askmaps-doc
AutoReqProv:    No

%description -n texlive-askmaps-doc
Documentation for askmaps

%package -n texlive-aspectratio
Provides:       tex-aspectratio = %{tl_version}
License:        LPPL
Summary:        Capital A and capital R ligature for Aspect Ratio
Version:        svn25243.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(aspectratio.map) = %{tl_version}, tex(amarbi.tfm) = %{tl_version}
Provides:       tex(amarri.tfm) = %{tl_version}, tex(aparbi.tfm) = %{tl_version}
Provides:       tex(aparri.tfm) = %{tl_version}, tex(ar10.tfm) = %{tl_version}
Provides:       tex(ar12.tfm) = %{tl_version}, tex(ar5.tfm) = %{tl_version}
Provides:       tex(ar6.tfm) = %{tl_version}, tex(ar7.tfm) = %{tl_version}
Provides:       tex(ar8.tfm) = %{tl_version}, tex(ar9.tfm) = %{tl_version}
Provides:       tex(arb10.tfm) = %{tl_version}, tex(arb12.tfm) = %{tl_version}
Provides:       tex(arb5.tfm) = %{tl_version}, tex(arb6.tfm) = %{tl_version}
Provides:       tex(arb7.tfm) = %{tl_version}, tex(arb8.tfm) = %{tl_version}
Provides:       tex(arb9.tfm) = %{tl_version}, tex(arssbi10.tfm) = %{tl_version}
Provides:       tex(arssi10.tfm) = %{tl_version}, tex(artti10.tfm) = %{tl_version}
Provides:       tex(amarbi.pfb) = %{tl_version}, tex(amarri.pfb) = %{tl_version}
Provides:       tex(ar10.pfb) = %{tl_version}, tex(ar12.pfb) = %{tl_version}
Provides:       tex(ar5.pfb) = %{tl_version}, tex(ar6.pfb) = %{tl_version}
Provides:       tex(ar7.pfb) = %{tl_version}, tex(ar8.pfb) = %{tl_version}
Provides:       tex(ar9.pfb) = %{tl_version}, tex(arb10.pfb) = %{tl_version}
Provides:       tex(arb12.pfb) = %{tl_version}, tex(arb5.pfb) = %{tl_version}
Provides:       tex(arb6.pfb) = %{tl_version}, tex(arb7.pfb) = %{tl_version}
Provides:       tex(arb8.pfb) = %{tl_version}, tex(arb9.pfb) = %{tl_version}
Provides:       tex(arssbi10.pfb) = %{tl_version}, tex(arssi10.pfb) = %{tl_version}
Provides:       tex(artti10.pfb) = %{tl_version}, tex(ar.sty) = %{tl_version}

%description -n texlive-aspectratio
The package provides fonts (both as Adobe Type 1 format, and as
Metafont source) for the 'AR' symbol (for Aspect Ratio) used by
aeronautical scientists and engineers. Note that the package
supersedes the package ar

%package -n texlive-aspectratio-doc
Summary:        Documentation for aspectratio
Version:        svn25243.2.0

Provides:       tex-aspectratio-doc
AutoReqProv:    No

%description -n texlive-aspectratio-doc
Documentation for aspectratio

%package -n texlive-assignment
Provides:       tex-assignment = %{tl_version}
License:        LPPL
Summary:        A class file for typesetting homework and lab assignments
Version:        svn20431.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(assignment.cls) = %{tl_version}

%description -n texlive-assignment
A class file for typesetting homework and lab assignments.

%package -n texlive-assignment-doc
Summary:        Documentation for assignment
Version:        svn20431.0

Provides:       tex-assignment-doc
AutoReqProv:    No

%description -n texlive-assignment-doc
Documentation for assignment

%package -n texlive-assoccnt
Provides:       tex-assoccnt = %{tl_version}
License:        LPPL 1.3
Summary:        Associate counters, making them step when a master steps
Version:        svn38497

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(etoolbox.sty), tex(xkeyval.sty), tex(xstring.sty)
Provides:       tex(assoccnt.sty) = %{tl_version}

%description -n texlive-assoccnt
The package provides the means of declaring a set of counters
to be stepped, each time some 'master' counter is stepped.

%package -n texlive-assoccnt-doc
Summary:        Documentation for assoccnt
Version:        svn38497

Provides:       tex-assoccnt-doc
AutoReqProv:    No

%description -n texlive-assoccnt-doc
Documentation for assoccnt

%package -n texlive-astro
Provides:       tex-astro = %{tl_version}
License:        LPPL
Summary:        Astronomical (planetary) symbols
Version:        svn15878.2.20

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(astrosym.tfm) = %{tl_version}

%description -n texlive-astro
Astrosym is a font containing astronomical symbols, including
those used for the planets, four planetoids, the phases of the
moon, the signs of the zodiac, and some additional symbols. The
font is distributed as Metafont source.

%package -n texlive-astro-doc
Summary:        Documentation for astro
Version:        svn15878.2.20

Provides:       tex-astro-doc
AutoReqProv:    No

%description -n texlive-astro-doc
Documentation for astro

%package -n texlive-asyfig
Provides:       tex-asyfig = %{tl_version}
License:        LPPL
Summary:        Commands for using Asymptote figures
Version:        svn17512.0.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(ifmtarg.sty)
Provides:       tex(asyalign.sty) = %{tl_version}, tex(asyfig.sty) = %{tl_version}
Provides:       tex(asyprocess.sty) = %{tl_version}

%description -n texlive-asyfig
The package provides a means of reading Asymptote figures from
separate files, rather than within the document, as is standard
in the asymptote package, which is provided as part of the
Asymptote bundle. The asymptote way can prove cumbersome in a
large document; the present package allows the user to process
one picture at a time, in simple test documents, and then to
migrate (with no fuss) to their use in the target document.

%package -n texlive-asyfig-doc
Summary:        Documentation for asyfig
Version:        svn17512.0.1c

Provides:       tex-asyfig-doc
AutoReqProv:    No

%description -n texlive-asyfig-doc
Documentation for asyfig

%package -n texlive-asypictureb
Provides:       tex-asypictureb = %{tl_version}
License:        LPPL 1.3
Summary:        User-friendly integration of Asymptote into LaTeX
Version:        svn33490.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyvrb.sty), tex(graphicx.sty), tex(pgfkeys.sty), tex(ifplatform.sty)
Requires:       tex(verbatimcopy.sty)
Provides:       tex(asypictureB.sty) = %{tl_version}

%description -n texlive-asypictureb
The package is an unofficial alternative to the package
provided with the Asymptote distribution, for including
pictures within a LaTeX source file. While it does not
duplicate all the features of the official package, this
package is more user-friendly in several ways. Most notably,
Asymptote errors are repackaged as LaTeX errors, making
debugging less of a pain. It also has a more robust mechanism
for identifying unchanged pictures that need not be recompiled.

%package -n texlive-asypictureb-doc
Summary:        Documentation for asypictureb
Version:        svn33490.0.3

Provides:       tex-asypictureb-doc
AutoReqProv:    No

%description -n texlive-asypictureb-doc
Documentation for asypictureb

%package -n texlive-attachfile
Provides:       tex-attachfile = %{tl_version}
License:        LPPL 1.3
Summary:        Attach arbitrary files to a PDF document
Version:        svn42099
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(keyval.sty), tex(calc.sty), tex(color.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(attachfile.sty) = %{tl_version}

%description -n texlive-attachfile
Starting with PDF 1.3 (Adobe Acrobat 4.0), PDF files can
contain file attachments -- arbitrary files that a reader can
extract, just like attachments to an e-mail message. The
attachfile package brings this functionality to pdfLaTeX and
provides some additional features not available in Acrobat,
such as the ability to use arbitrary LaTeX code for the file
icon -- including things like \includegraphics, tabular, and
mathematics. Settings can be made either globally or on a per-
attachment basis. Attachfile makes it easy to attach files and
customize their appearance in the enclosing document. The
package supports the Created, Modified, and Size keys in the
EmbeddedFile's Params dictionary.

%package -n texlive-attachfile-doc
Summary:        Documentation for attachfile
Version:        svn42099
Provides:       tex-attachfile-doc
AutoReqProv:    No

%description -n texlive-attachfile-doc
Documentation for attachfile

%package -n texlive-augie
Provides:       tex-augie = %{tl_version}
License:        LPPL
Summary:        Calligraphic font for typesetting handwriting
Version:        svn18948.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(augie.map) = %{tl_version}, tex(augie7t.tfm) = %{tl_version}
Provides:       tex(augie8c.tfm) = %{tl_version}, tex(augie8r.tfm) = %{tl_version}
Provides:       tex(augie8t.tfm) = %{tl_version}, tex(augie___.tfm) = %{tl_version}
Provides:       tex(augie___.pfb) = %{tl_version}, tex(augie7t.vf) = %{tl_version}
Provides:       tex(augie8c.vf) = %{tl_version}, tex(augie8t.vf) = %{tl_version}
Provides:       tex(ot1augie.fd) = %{tl_version}, tex(t1augie.fd) = %{tl_version}
Provides:       tex(ts1augie.fd) = %{tl_version}

%description -n texlive-augie
A calligraphic font for simulating American-style informal
handwriting. The font is distributed in Adobe Type 1 format.

%package -n texlive-augie-doc
Summary:        Documentation for augie
Version:        svn18948.0

Provides:       tex-augie-doc
AutoReqProv:    No

%description -n texlive-augie-doc
Documentation for augie

%package -n texlive-auncial-new
Provides:       tex-auncial-new = %{tl_version}
License:        LPPL
Summary:        Artificial Uncial font and LaTeX support macros
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(auncial.map) = %{tl_version}, tex(auncl10.tfm) = %{tl_version}
Provides:       tex(aunclb10.tfm) = %{tl_version}, tex(auncl10.pfb) = %{tl_version}
Provides:       tex(aunclb10.pfb) = %{tl_version}, tex(allauncl.sty) = %{tl_version}
Provides:       tex(auncial.sty) = %{tl_version}, tex(b1auncl.fd) = %{tl_version}

%description -n texlive-auncial-new
The auncial-new bundle provides packages and fonts for a script
based on the Artificial Uncial manuscript book-hand used
between the 6th & 10th century AD. The script consists of
minuscules and digits, with some appropriate period punctuation
marks. Both normal and bold versions are provided, and the font
is distributed in Adobe Type 1 format. This is an experimental
new version of the auncial bundle, which is one of a series of
bookhand fonts. The font follows the B1 encoding developed for
bookhands. Access to the encoding is essential. The encoding
mainly follows the standard T1 encoding.

%package -n texlive-auncial-new-doc
Summary:        Documentation for auncial-new
Version:        svn15878.2.0

Provides:       tex-auncial-new-doc
AutoReqProv:    No

%description -n texlive-auncial-new-doc
Documentation for auncial-new

%package -n texlive-aurical
Provides:       tex-aurical = %{tl_version}
License:        LPPL
Summary:        Calligraphic fonts for use with LaTeX in T1 encoding
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(aurical.map) = %{tl_version}, tex(AmiciLogo.tfm) = %{tl_version}
Provides:       tex(AmiciLogoBold.tfm) = %{tl_version}, tex(AmiciLogoBoldRslant.tfm) = %{tl_version}
Provides:       tex(AmiciLogoBoldSlant.tfm) = %{tl_version}
Provides:       tex(AmiciLogoRslant.tfm) = %{tl_version}
Provides:       tex(AmiciLogoSlant.tfm) = %{tl_version}, tex(AuriocusKalligraphicus.tfm) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusBold.tfm) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusBoldRslant.tfm) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusBoldSlant.tfm) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusRslant.tfm) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusSlant.tfm) = %{tl_version}
Provides:       tex(JanaSkrivana.tfm) = %{tl_version}, tex(JanaSkrivanaBold.tfm) = %{tl_version}
Provides:       tex(JanaSkrivanaBoldRslant.tfm) = %{tl_version}
Provides:       tex(JanaSkrivanaBoldSlant.tfm) = %{tl_version}
Provides:       tex(JanaSkrivanaRslant.tfm) = %{tl_version}
Provides:       tex(JanaSkrivanaSlant.tfm) = %{tl_version}
Provides:       tex(LukasSvatba.tfm) = %{tl_version}, tex(LukasSvatbaBold.tfm) = %{tl_version}
Provides:       tex(LukasSvatbaBoldRslant.tfm) = %{tl_version}
Provides:       tex(LukasSvatbaBoldSlant.tfm) = %{tl_version}
Provides:       tex(LukasSvatbaRslant.tfm) = %{tl_version}
Provides:       tex(LukasSvatbaSlant.tfm) = %{tl_version}
Provides:       tex(AmiciLogo.pfb) = %{tl_version}, tex(AmiciLogoBold.pfb) = %{tl_version}
Provides:       tex(AmiciLogoBoldRslant.pfb) = %{tl_version}
Provides:       tex(AmiciLogoBoldSlant.pfb) = %{tl_version}
Provides:       tex(AmiciLogoRslant.pfb) = %{tl_version}
Provides:       tex(AmiciLogoSlant.pfb) = %{tl_version}, tex(AuriocusKalligraphicus.pfb) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusBold.pfb) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusBoldRslant.pfb) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusBoldSlant.pfb) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusRslant.pfb) = %{tl_version}
Provides:       tex(AuriocusKalligraphicusSlant.pfb) = %{tl_version}
Provides:       tex(JanaSkrivana.pfb) = %{tl_version}, tex(JanaSkrivanaBold.pfb) = %{tl_version}
Provides:       tex(JanaSkrivanaBoldRslant.pfb) = %{tl_version}
Provides:       tex(JanaSkrivanaBoldSlant.pfb) = %{tl_version}
Provides:       tex(JanaSkrivanaRslant.pfb) = %{tl_version}
Provides:       tex(JanaSkrivanaSlant.pfb) = %{tl_version}
Provides:       tex(LukasSvatba.pfb) = %{tl_version}, tex(LukasSvatbaBold.pfb) = %{tl_version}
Provides:       tex(LukasSvatbaBoldRslant.pfb) = %{tl_version}
Provides:       tex(LukasSvatbaBoldSlant.pfb) = %{tl_version}
Provides:       tex(LukasSvatbaRslant.pfb) = %{tl_version}
Provides:       tex(LukasSvatbaSlant.pfb) = %{tl_version}
Provides:       tex(T1AmiciLogo.fd) = %{tl_version}, tex(T1AuriocusKalligraphicus.fd) = %{tl_version}
Provides:       tex(T1JanaSkrivana.fd) = %{tl_version}, tex(T1LukasSvatba.fd) = %{tl_version}
Provides:       tex(aurical.sty) = %{tl_version}

%description -n texlive-aurical
The package that implements a set (AuriocusKalligraphicus) of
three calligraphic fonts derived from the author's handwriting
in Adobe Type 1 Format, T1 encoding for use with LaTeX:
Auriocus Kalligraphicus; Lukas Svatba; and Jana Skrivana. Each
font features oldstyle digits and (machine-generated) boldface
and slanted versions. A variant of Lukas Svatba offers a 'long
s'.

%package -n texlive-aurical-doc
Summary:        Documentation for aurical
Version:        svn15878.1.5

Provides:       tex-aurical-doc
AutoReqProv:    No

%description -n texlive-aurical-doc
Documentation for aurical

%package -n texlive-authoraftertitle
Provides:       tex-authoraftertitle = %{tl_version}
License:        Public Domain
Summary:        Make author, etc., available after \maketitle
Version:        svn24863.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(authoraftertitle.sty) = %{tl_version}

%description -n texlive-authoraftertitle
This jiffy package makes the author, title and date of the
package available to the user (as \MyAuthor, etc) after the
\maketitle command has been executed.

%package -n texlive-authoraftertitle-doc
Summary:        Documentation for authoraftertitle
Version:        svn24863.0.9

Provides:       tex-authoraftertitle-doc
AutoReqProv:    No

%description -n texlive-authoraftertitle-doc
Documentation for authoraftertitle

%package -n texlive-autoarea
Provides:       tex-autoarea = %{tl_version}
License:        LPPL
Summary:        Automatic computation of bounding boxes with PiCTeX
Version:        svn15878.0.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(autoarea.sty) = %{tl_version}

%description -n texlive-autoarea
This package makes PiCTeX recognize lines and arcs in
determining the "bounding box" of a picture. (PiCTeX so far
accounted for put commands only). The "bounding box" is
essential for proper placement of a picture between running
text and margins and for keeping the running text away.

%package -n texlive-autoarea-doc
Summary:        Documentation for autoarea
Version:        svn15878.0.3a

Provides:       tex-autoarea-doc
AutoReqProv:    No

%description -n texlive-autoarea-doc
Documentation for autoarea

%package -n texlive-automata
Provides:       tex-automata = %{tl_version}
License:        LPPL
Summary:        Finite state machines, graphs and trees in MetaPost
Version:        svn19717.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-automata
The package offers a collection of macros for MetaPost to make
easier to draw finite-state machines, automata, labelled
graphs, etc. The user defines nodes, which may be isolated or
arranged into matrices or trees; edges connect pairs of nodes
through arbitrary paths. Parameters, that specify the shapes of
nodes and the styles of edges, may be adjusted.

%package -n texlive-automata-doc
Summary:        Documentation for automata
Version:        svn19717.0.3

Provides:       tex-automata-doc
AutoReqProv:    No

%description -n texlive-automata-doc
Documentation for automata

%package -n texlive-autonum
Provides:       tex-autonum = %{tl_version}
License:        LPPL 1.3
Summary:        Automatic equation references
Version:        svn36084.0.3.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(etextools.sty), tex(amsmath.sty), tex(textpos.sty)
Requires:       tex(letltxmacro.sty)
Provides:       tex(autonum.sty) = %{tl_version}

%description -n texlive-autonum
The package arranges that equation numbers are applied only to
those equations that are referenced. This operation is similar
to the showonlyrefs option of the package mathtools.

%package -n texlive-autonum-doc
Summary:        Documentation for autonum
Version:        svn36084.0.3.11

Provides:       tex-autonum-doc
AutoReqProv:    No

%description -n texlive-autonum-doc
Documentation for autonum

%package -n texlive-autopdf
Provides:       tex-autopdf = %{tl_version}
License:        LPPL 1.2
Summary:        Conversion of graphics to pdfLaTeX-compatible formats
Version:        svn32377.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(ifthen.sty), tex(ifpdf.sty), tex(ifplatform.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(autopdf.sty) = %{tl_version}

%description -n texlive-autopdf
The package facilitates the on-the-fly conversion of various
graphics formats to formats supported by pdfLaTeX (e.g. PDF).
It uses a range of external programs, and therefore requires
that the LaTeX run starts with write18 enabled.

%package -n texlive-autopdf-doc
Summary:        Documentation for autopdf
Version:        svn32377.1.1

Provides:       tex-autopdf-doc
AutoReqProv:    No

%description -n texlive-autopdf-doc
Documentation for autopdf

%package -n texlive-auto-pst-pdf
Provides:       tex-auto-pst-pdf = %{tl_version}
License:        LPPL
Summary:        Wrapper for pst-pdf (with some psfrag features)
Version:        svn23723.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(xkeyval.sty), tex(ifplatform.sty), tex(pst-pdf.sty)
Provides:       tex(auto-pst-pdf.sty) = %{tl_version}

%description -n texlive-auto-pst-pdf
The package uses --shell-escape to execute pst-pdf when
necessary. This makes it especially easy to integrate into the
workflow of an editor with just "LaTeX" and "pdfLaTeX" buttons.
Wrappers are provided for various psfrag-related features so
that Matlab figures via laprint, Mathematica figures via
MathPSfrag, and regular psfrag figures can all be input
consistently and easily.

%package -n texlive-auto-pst-pdf-doc
Summary:        Documentation for auto-pst-pdf
Version:        svn23723.0.6

Provides:       tex-auto-pst-pdf-doc
AutoReqProv:    No

%description -n texlive-auto-pst-pdf-doc
Documentation for auto-pst-pdf

%package -n texlive-avantgar
Provides:       tex-avantgar = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(uag.map) = %{tl_version}, tex(pagd.tfm) = %{tl_version}
Provides:       tex(pagd7t.tfm) = %{tl_version}, tex(pagd8c.tfm) = %{tl_version}
Provides:       tex(pagd8r.tfm) = %{tl_version}, tex(pagd8t.tfm) = %{tl_version}
Provides:       tex(pagdc.tfm) = %{tl_version}, tex(pagdc7t.tfm) = %{tl_version}
Provides:       tex(pagdc8t.tfm) = %{tl_version}, tex(pagdo.tfm) = %{tl_version}
Provides:       tex(pagdo7t.tfm) = %{tl_version}, tex(pagdo8c.tfm) = %{tl_version}
Provides:       tex(pagdo8r.tfm) = %{tl_version}, tex(pagdo8t.tfm) = %{tl_version}
Provides:       tex(pagk.tfm) = %{tl_version}, tex(pagk7t.tfm) = %{tl_version}
Provides:       tex(pagk8c.tfm) = %{tl_version}, tex(pagk8r.tfm) = %{tl_version}
Provides:       tex(pagk8t.tfm) = %{tl_version}, tex(pagkc.tfm) = %{tl_version}
Provides:       tex(pagkc7t.tfm) = %{tl_version}, tex(pagkc8t.tfm) = %{tl_version}
Provides:       tex(pagko.tfm) = %{tl_version}, tex(pagko7t.tfm) = %{tl_version}
Provides:       tex(pagko8c.tfm) = %{tl_version}, tex(pagko8r.tfm) = %{tl_version}
Provides:       tex(pagko8t.tfm) = %{tl_version}, tex(uagb7t.tfm) = %{tl_version}
Provides:       tex(uagb8c.tfm) = %{tl_version}, tex(uagb8r.tfm) = %{tl_version}
Provides:       tex(uagb8t.tfm) = %{tl_version}, tex(uagbc7t.tfm) = %{tl_version}
Provides:       tex(uagbc8t.tfm) = %{tl_version}, tex(uagbi7t.tfm) = %{tl_version}
Provides:       tex(uagbi8c.tfm) = %{tl_version}, tex(uagbi8r.tfm) = %{tl_version}
Provides:       tex(uagbi8t.tfm) = %{tl_version}, tex(uagbo7t.tfm) = %{tl_version}
Provides:       tex(uagbo8c.tfm) = %{tl_version}, tex(uagbo8r.tfm) = %{tl_version}
Provides:       tex(uagbo8t.tfm) = %{tl_version}, tex(uagd7t.tfm) = %{tl_version}
Provides:       tex(uagd8c.tfm) = %{tl_version}, tex(uagd8r.tfm) = %{tl_version}
Provides:       tex(uagd8t.tfm) = %{tl_version}, tex(uagdc7t.tfm) = %{tl_version}
Provides:       tex(uagdc8t.tfm) = %{tl_version}, tex(uagdo7t.tfm) = %{tl_version}
Provides:       tex(uagdo8c.tfm) = %{tl_version}, tex(uagdo8r.tfm) = %{tl_version}
Provides:       tex(uagdo8t.tfm) = %{tl_version}, tex(uagk7t.tfm) = %{tl_version}
Provides:       tex(uagk8c.tfm) = %{tl_version}, tex(uagk8r.tfm) = %{tl_version}
Provides:       tex(uagk8t.tfm) = %{tl_version}, tex(uagkc7t.tfm) = %{tl_version}
Provides:       tex(uagkc8t.tfm) = %{tl_version}, tex(uagko7t.tfm) = %{tl_version}
Provides:       tex(uagko8c.tfm) = %{tl_version}, tex(uagko8r.tfm) = %{tl_version}
Provides:       tex(uagko8t.tfm) = %{tl_version}, tex(uagr7t.tfm) = %{tl_version}
Provides:       tex(uagr8c.tfm) = %{tl_version}, tex(uagr8r.tfm) = %{tl_version}
Provides:       tex(uagr8t.tfm) = %{tl_version}, tex(uagrc7t.tfm) = %{tl_version}
Provides:       tex(uagrc8t.tfm) = %{tl_version}, tex(uagri7t.tfm) = %{tl_version}
Provides:       tex(uagri8c.tfm) = %{tl_version}, tex(uagri8r.tfm) = %{tl_version}
Provides:       tex(uagri8t.tfm) = %{tl_version}, tex(uagro7t.tfm) = %{tl_version}
Provides:       tex(uagro8c.tfm) = %{tl_version}, tex(uagro8r.tfm) = %{tl_version}
Provides:       tex(uagro8t.tfm) = %{tl_version}, tex(uagd8a.pfb) = %{tl_version}
Provides:       tex(uagdo8a.pfb) = %{tl_version}, tex(uagk8a.pfb) = %{tl_version}
Provides:       tex(uagko8a.pfb) = %{tl_version}, tex(pagd.vf) = %{tl_version}
Provides:       tex(pagd7t.vf) = %{tl_version}, tex(pagd8c.vf) = %{tl_version}
Provides:       tex(pagd8t.vf) = %{tl_version}, tex(pagdc.vf) = %{tl_version}
Provides:       tex(pagdc7t.vf) = %{tl_version}, tex(pagdc8t.vf) = %{tl_version}
Provides:       tex(pagdo.vf) = %{tl_version}, tex(pagdo7t.vf) = %{tl_version}
Provides:       tex(pagdo8c.vf) = %{tl_version}, tex(pagdo8t.vf) = %{tl_version}
Provides:       tex(pagk.vf) = %{tl_version}, tex(pagk7t.vf) = %{tl_version}
Provides:       tex(pagk8c.vf) = %{tl_version}, tex(pagk8t.vf) = %{tl_version}
Provides:       tex(pagkc.vf) = %{tl_version}, tex(pagkc7t.vf) = %{tl_version}
Provides:       tex(pagkc8t.vf) = %{tl_version}, tex(pagko.vf) = %{tl_version}
Provides:       tex(pagko7t.vf) = %{tl_version}, tex(pagko8c.vf) = %{tl_version}
Provides:       tex(pagko8t.vf) = %{tl_version}, tex(uagb7t.vf) = %{tl_version}
Provides:       tex(uagb8c.vf) = %{tl_version}, tex(uagb8t.vf) = %{tl_version}
Provides:       tex(uagbc7t.vf) = %{tl_version}, tex(uagbc8t.vf) = %{tl_version}
Provides:       tex(uagbi7t.vf) = %{tl_version}, tex(uagbi8c.vf) = %{tl_version}
Provides:       tex(uagbi8t.vf) = %{tl_version}, tex(uagbo7t.vf) = %{tl_version}
Provides:       tex(uagbo8c.vf) = %{tl_version}, tex(uagbo8t.vf) = %{tl_version}
Provides:       tex(uagd7t.vf) = %{tl_version}, tex(uagd8c.vf) = %{tl_version}
Provides:       tex(uagd8t.vf) = %{tl_version}, tex(uagdc7t.vf) = %{tl_version}
Provides:       tex(uagdc8t.vf) = %{tl_version}, tex(uagdo7t.vf) = %{tl_version}
Provides:       tex(uagdo8c.vf) = %{tl_version}, tex(uagdo8t.vf) = %{tl_version}
Provides:       tex(uagk7t.vf) = %{tl_version}, tex(uagk8c.vf) = %{tl_version}
Provides:       tex(uagk8t.vf) = %{tl_version}, tex(uagkc7t.vf) = %{tl_version}
Provides:       tex(uagkc8t.vf) = %{tl_version}, tex(uagko7t.vf) = %{tl_version}
Provides:       tex(uagko8c.vf) = %{tl_version}, tex(uagko8t.vf) = %{tl_version}
Provides:       tex(uagr7t.vf) = %{tl_version}, tex(uagr8c.vf) = %{tl_version}
Provides:       tex(uagr8t.vf) = %{tl_version}, tex(uagrc7t.vf) = %{tl_version}
Provides:       tex(uagrc8t.vf) = %{tl_version}, tex(uagri7t.vf) = %{tl_version}
Provides:       tex(uagri8c.vf) = %{tl_version}, tex(uagri8t.vf) = %{tl_version}
Provides:       tex(uagro7t.vf) = %{tl_version}, tex(uagro8c.vf) = %{tl_version}
Provides:       tex(uagro8t.vf) = %{tl_version}, tex(8ruag.fd) = %{tl_version}
Provides:       tex(omluag.fd) = %{tl_version}, tex(omsuag.fd) = %{tl_version}
Provides:       tex(ot1uag.fd) = %{tl_version}, tex(t1uag.fd) = %{tl_version}
Provides:       tex(ts1uag.fd) = %{tl_version}

%description -n texlive-avantgar
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-avremu
Provides:       tex-avremu = %{tl_version}
License:        LPPL 1.3
Summary:        An 8-Bit Microcontroller Simulator written in LaTeX
Version:        svn35373.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(tabularx.sty), tex(kvoptions.sty)
Provides:       tex(avr.binary.tex) = %{tl_version}, tex(avr.bitops.tex) = %{tl_version}
Provides:       tex(avr.draw.tex) = %{tl_version}, tex(avr.instr.tex) = %{tl_version}
Provides:       tex(avr.io.tex) = %{tl_version}, tex(avr.memory.tex) = %{tl_version}
Provides:       tex(avr.numbers.tex) = %{tl_version}, tex(avr.testsuite.tex) = %{tl_version}
Provides:       tex(avremu.sty) = %{tl_version}

%description -n texlive-avremu
A fully working package to simulate a Microprocessor in pure
LaTeX. The simulator is able to calculate complex pictures,
like Mandelbrot sets.

%package -n texlive-avremu-doc
Summary:        Documentation for avremu
Version:        svn35373.0.1

Provides:       tex-avremu-doc
AutoReqProv:    No

%description -n texlive-avremu-doc
Documentation for avremu

%package -n texlive-b1encoding
Provides:       tex-b1encoding = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX encoding tools for Bookhands fonts
Version:        svn21271.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(TeXB1.enc) = %{tl_version}, tex(b1cmr.fd) = %{tl_version}
Provides:       tex(b1enc.def) = %{tl_version}

%description -n texlive-b1encoding
The package characterises and defines the author's B1 encoding
for use with LaTeX when typesetting things using his Bookhands
fonts.

%package -n texlive-b1encoding-doc
Summary:        Documentation for b1encoding
Version:        svn21271.1.0

Provides:       tex-b1encoding-doc
AutoReqProv:    No

%description -n texlive-b1encoding-doc
Documentation for b1encoding

%package -n texlive-babel-albanian
Provides:       tex-babel-albanian = %{tl_version}
License:        LPPL
Summary:        Support for Albanian within babel
Version:        svn30254.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(albanian.ldf) = %{tl_version}

%description -n texlive-babel-albanian
The package provides support for typesetting Albanian (as part
of the babel system).

%package -n texlive-babel-albanian-doc
Summary:        Documentation for babel-albanian
Version:        svn30254.1.0c

Provides:       tex-babel-albanian-doc
AutoReqProv:    No

%description -n texlive-babel-albanian-doc
Documentation for babel-albanian

%package -n texlive-babel-bahasa
Provides:       tex-babel-bahasa = %{tl_version}
License:        LPPL 1.3
Summary:        Support for Bahasa within babel
Version:        svn30255.1.0l.metapackage
Requires:       texlive-babel-indonesian, texlive-babel-malay

%description -n texlive-babel-bahasa
This metapackage pulls in texlive-babel-indonesian and texlive-babel-malay.

%package -n texlive-babel-bahasa-doc
Summary:        Documentation for babel-bahasa
Version:        svn30255.1.0l.metapackage
Provides:       tex-babel-bahasa-doc
Requires:       texlive-babel-indonesian-doc, texlive-babel-malay-doc

%description -n texlive-babel-bahasa-doc
Metapackage, pulls in texlive-babel-indonesian-doc and texlive-babel-malay-doc.

%package -n texlive-babel-indonesian
Provides:       tex-babel-indonesian = %{tl_version}
License:        LPPL 1.3
Summary:        Support for Indonesian within babel
Version:        svn43235
Requires:       texlive-base, texlive-kpathsea
Provides:       tex(bahasa.ldf) = %{tl_version}, tex(bahasai.ldf) = %{tl_version}
Provides:       tex(indon.ldf) = %{tl_version}, tex(indonesian.ldf) = %{tl_version}

%description -n texlive-babel-indonesian
Support for Indonesian within babel.

%package -n texlive-babel-indonesian-doc
Summary:        Documentation for babel-indonesian
Version:        svn43235

Provides:       tex-babel-indonesian-doc

%description -n texlive-babel-indonesian-doc
Documentation for babel-indonesian.

%package -n texlive-babel-malay
Provides:       tex-babel-malay = %{tl_version}
License:        LPPL 1.3
Summary:        Support for Malay within babel
Version:        svn43234

Requires:       texlive-base, texlive-kpathsea
Provides:       tex(bahasam.ldf) = %{tl_version}, tex(malay.ldf) = %{tl_version}
Provides:       tex(melayu.ldf) = %{tl_version}, tex(meyalu.ldf) = %{tl_version}

%description -n texlive-babel-malay
Support for Malay within babel.

%package -n texlive-babel-malay-doc
Summary:        Documentation for babel-malay
Version:        svn43235

Provides:       tex-babel-malay-doc

%description -n texlive-babel-malay-doc
Documentation for babel-malay.

%package -n texlive-babel-basque
Provides:       tex-babel-basque = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Basque
Version:        svn30256.1.0f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(basque.ldf) = %{tl_version}

%description -n texlive-babel-basque
The package establishes Basque conventions in a document.

%package -n texlive-babel-basque-doc
Summary:        Documentation for babel-basque
Version:        svn30256.1.0f

Provides:       tex-babel-basque-doc
AutoReqProv:    No

%description -n texlive-babel-basque-doc
Documentation for babel-basque

%package -n texlive-babelbib
Provides:       tex-babelbib = %{tl_version}
License:        LPPL
Summary:        Multilingual bibliographies
Version:        svn25245.1.31

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(babel.sty)
Provides:       tex(babelbib.sty) = %{tl_version}

%description -n texlive-babelbib
This package enables to generate multilingual bibliographies in
cooperation with babel. Two approaches are possible: Each
citation may be written in another language, or the whole
bibliography can be typeset in a language chosen by the user.
In addition, the package supports commands to change the
typography of the bibliographies.

%package -n texlive-babelbib-doc
Summary:        Documentation for babelbib
Version:        svn25245.1.31

Provides:       tex-babelbib-doc
AutoReqProv:    No

%description -n texlive-babelbib-doc
Documentation for babelbib

%package -n texlive-babel-bosnian
Provides:       tex-babel-bosnian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contrib support for Bosnian
Version:        svn38174.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bosnian.ldf) = %{tl_version}

%description -n texlive-babel-bosnian
The package provides a language definition file that enables
support of Bosnian with babel.

%package -n texlive-babel-bosnian-doc
Summary:        Documentation for babel-bosnian
Version:        svn38174.1.1

Provides:       tex-babel-bosnian-doc
AutoReqProv:    No

%description -n texlive-babel-bosnian-doc
Documentation for babel-bosnian

%package -n texlive-babel-breton
Provides:       tex-babel-breton = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Breton
Version:        svn30257.1.0h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(breton.ldf) = %{tl_version}

%description -n texlive-babel-breton
Breton (being, principally, a spoken language) does not have
typographic rules of its own; this package provides an
"appropriate" selection of French and British typographic
rules.

%package -n texlive-babel-breton-doc
Summary:        Documentation for babel-breton
Version:        svn30257.1.0h

Provides:       tex-babel-breton-doc
AutoReqProv:    No

%description -n texlive-babel-breton-doc
Documentation for babel-breton

%package -n texlive-babel-bulgarian
Provides:       tex-babel-bulgarian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Bulgarian
Version:        svn31902.1.2g

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bulgarian.ldf) = %{tl_version}

%description -n texlive-babel-bulgarian
The package provides support for documents in Bulgarian (or
simply containing some Bulgarian text).

%package -n texlive-babel-bulgarian-doc
Summary:        Documentation for babel-bulgarian
Version:        svn31902.1.2g

Provides:       tex-babel-bulgarian-doc
AutoReqProv:    No

%description -n texlive-babel-bulgarian-doc
Documentation for babel-bulgarian

%package -n texlive-babel-catalan
Provides:       tex-babel-catalan = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Catalan
Version:        svn30259.2.2p

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(catalan.ldf) = %{tl_version}

%description -n texlive-babel-catalan
The package establishes Catalan conventions in a document (or a
subset of the conventions, if Catalan is not the main language
of the document).

%package -n texlive-babel-catalan-doc
Summary:        Documentation for babel-catalan
Version:        svn30259.2.2p

Provides:       tex-babel-catalan-doc
AutoReqProv:    No

%description -n texlive-babel-catalan-doc
Documentation for babel-catalan

%package -n texlive-babel-croatian
Provides:       tex-babel-croatian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Croatian
Version:        svn35198.1.3l

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(croatian.ldf) = %{tl_version}

%description -n texlive-babel-croatian
The package establishes Croatian conventions in a document (or
a subset of the conventions, if Croatian is not the main
language of the document).

%package -n texlive-babel-croatian-doc
Summary:        Documentation for babel-croatian
Version:        svn35198.1.3l

Provides:       tex-babel-croatian-doc
AutoReqProv:    No

%description -n texlive-babel-croatian-doc
Documentation for babel-croatian

%package -n texlive-babel-czech
Provides:       tex-babel-czech = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Czech
Version:        svn30261.3.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(czech.ldf) = %{tl_version}, tex(czech.sty) = %{tl_version}

%description -n texlive-babel-czech
The package provides the language definition file for support
of Czech in babel. Some shortcuts are defined, as well as
translations to Czech of standard "LaTeX names".

%package -n texlive-babel-czech-doc
Summary:        Documentation for babel-czech
Version:        svn30261.3.1a

Provides:       tex-babel-czech-doc
AutoReqProv:    No

%description -n texlive-babel-czech-doc
Documentation for babel-czech

%package -n texlive-babel-danish
Provides:       tex-babel-danish = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Danish
Version:        svn30262.1.3r

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(danish.ldf) = %{tl_version}

%description -n texlive-babel-danish
The package provides a language definition, file for use with
babel, which establishes Danish conventions in a document (or a
subset of the conventions, if Danish is not the main language
of the document).

%package -n texlive-babel-danish-doc
Summary:        Documentation for babel-danish
Version:        svn30262.1.3r

Provides:       tex-babel-danish-doc
AutoReqProv:    No

%description -n texlive-babel-danish-doc
Documentation for babel-danish

%package -n texlive-babel-dutch
Provides:       tex-babel-dutch = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for Dutch
Version:        svn30263.3.8i

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dutch.ldf) = %{tl_version}

%description -n texlive-babel-dutch
The package provides a language definition, file for use with
babel, which establishes Dutch conventions in a document (or a
subset of the conventions, if Dutch is not the main language of
the document).

%package -n texlive-babel-dutch-doc
Summary:        Documentation for babel-dutch
Version:        svn30263.3.8i

Provides:       tex-babel-dutch-doc
AutoReqProv:    No

%description -n texlive-babel-dutch-doc
Documentation for babel-dutch

%package -n texlive-babel-english
Provides:       tex-babel-english = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for English
Version:        svn44495
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(english.ldf) = %{tl_version}

%description -n texlive-babel-english
The package provides the language definition file for support
of English in babel. Care is taken to select british
hyphenation patterns for British English and Australian text,
and default ('american') patterns for Canadian and USA text.

%package -n texlive-babel-english-doc
Summary:        Documentation for babel-english
Version:        svn44495
Provides:       tex-babel-english-doc
AutoReqProv:    No

%description -n texlive-babel-english-doc
Documentation for babel-english

%package -n texlive-babel-esperanto
Provides:       tex-babel-esperanto = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Esperanto
Version:        svn30265.1.4t

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(esperanto.ldf) = %{tl_version}

%description -n texlive-babel-esperanto
The package provides the language definition file for support
of Esperanto in babel. Some shortcuts are defined, as well as
translations to Esperanto of standard "LaTeX names".

%package -n texlive-babel-esperanto-doc
Summary:        Documentation for babel-esperanto
Version:        svn30265.1.4t

Provides:       tex-babel-esperanto-doc
AutoReqProv:    No

%description -n texlive-babel-esperanto-doc
Documentation for babel-esperanto

%package -n texlive-babel-estonian
Provides:       tex-babel-estonian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Estonian
Version:        svn38064.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(estonian.ldf) = %{tl_version}

%description -n texlive-babel-estonian
The package provides the language definition file for support
of Estonian in babel. Some shortcuts are defined, as well as
translations to Estonian of standard "LaTeX names".

%package -n texlive-babel-estonian-doc
Summary:        Documentation for babel-estonian
Version:        svn38064.1.1a

Provides:       tex-babel-estonian-doc
AutoReqProv:    No

%description -n texlive-babel-estonian-doc
Documentation for babel-estonian

%package -n texlive-babel-finnish
Provides:       tex-babel-finnish = %{tl_version}
License:        LPPL
Summary:        babel-finnish package
Version:        svn30267.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(finnish.ldf) = %{tl_version}

%description -n texlive-babel-finnish
babel-finnish package

%package -n texlive-babel-finnish-doc
Summary:        Documentation for babel-finnish
Version:        svn30267.0

Provides:       tex-babel-finnish-doc
AutoReqProv:    No

%description -n texlive-babel-finnish-doc
Documentation for babel-finnish

%package -n texlive-babel-french
Provides:       tex-babel-french = %{tl_version}
License:        LPPL 1.3
Summary:        Babel contributed support for French
Version:        svn48222
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(luatexbase.sty), tex(scalefnt.sty), tex(keyval.sty)
Provides:       tex(frenchb.ldf) = %{tl_version}

%description -n texlive-babel-french
The package establishes French conventions in a document (or a
subset of the conventions, if French is not the main language
of the document).

%package -n texlive-babel-french-doc
Summary:        Documentation for babel-french
Version:        svn48222
Provides:       tex-babel-french-doc
AutoReqProv:    No

%description -n texlive-babel-french-doc
Documentation for babel-french

%package -n texlive-babel-friulan
Provides:       tex-babel-friulan = %{tl_version}
License:        LPPL 1.3
Summary:        Babel/Polyglossia support for Friulan(Furlan)
Version:        svn39861

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(friulan.ldf) = %{tl_version}

%description -n texlive-babel-friulan
The package provides a language description file that enables
support of Friulan either with babel or with polyglossia.

%package -n texlive-babel-friulan-doc
Summary:        Documentation for babel-friulan
Version:        svn39861

Provides:       tex-babel-friulan-doc
AutoReqProv:    No

%description -n texlive-babel-friulan-doc
Documentation for babel-friulan

%package -n texlive-babel-galician
Provides:       tex-babel-galician = %{tl_version}
License:        LPPL
Summary:        babel-galician package
Version:        svn30270.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(galician.ldf) = %{tl_version}

%description -n texlive-babel-galician
babel-galician package

%package -n texlive-babel-galician-doc
Summary:        Documentation for babel-galician
Version:        svn30270.0

Provides:       tex-babel-galician-doc
AutoReqProv:    No

%description -n texlive-babel-galician-doc
Documentation for babel-galician

%package -n texlive-babel-georgian
Provides:       tex-babel-georgian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel
Version:        svn45864
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(georgian.ldf) = %{tl_version}, tex(georgian.sty) = %{tl_version}
Provides:       tex(georgiancaps.tex) = %{tl_version}

%description -n texlive-babel-georgian
The package provides support for use of Babel in documents
written in Georgian. The package is adapted for use both under
'traditional' TeX engines, and under XeTeX and LuaTeX.

%package -n texlive-babel-georgian-doc
Summary:        Documentation for babel-georgian
Version:        svn45864
Provides:       tex-babel-georgian-doc
AutoReqProv:    No

%description -n texlive-babel-georgian-doc
Documentation for babel-georgian

%package -n texlive-babel-german
Provides:       tex-babel-german = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for documents written in German
Version:        svn47192
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(austrian.ldf) = %{tl_version}, tex(german.ldf) = %{tl_version}
Provides:       tex(germanb.ldf) = %{tl_version}, tex(naustrian.ldf) = %{tl_version}
Provides:       tex(ngerman.ldf) = %{tl_version}, tex(ngermanb.ldf) = %{tl_version}
Provides:       tex(nswissgerman.ldf) = %{tl_version}, tex(swissgerman.ldf) = %{tl_version}

%description -n texlive-babel-german
The package defines LaTeX support, within the Babel package, of
German (including its Austrian dialect), in both 'old' and
'new' orthographies.

%package -n texlive-babel-german-doc
Summary:        Documentation for babel-german
Version:        svn47192
Provides:       tex-babel-german-doc
AutoReqProv:    No

%description -n texlive-babel-german-doc
Documentation for babel-german

%package -n texlive-babel-greek
Provides:       tex-babel-greek = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for documents written in Greek
Version:        svn42010
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(athnum.sty) = %{tl_version}, tex(greek.ldf) = %{tl_version}
Provides:       tex(grmath.sty) = %{tl_version}

%description -n texlive-babel-greek
The file provides modes for monotonic (single-diacritic) and
polytonic (multiple-diacritic) modes of writing. Provision is
made for Greek function names in mathematics, and for classical-
era symbols.

%package -n texlive-babel-greek-doc
Summary:        Documentation for babel-greek
Version:        svn42010
Provides:       tex-babel-greek-doc
AutoReqProv:    No

%description -n texlive-babel-greek-doc
Documentation for babel-greek

%package -n texlive-babel-hebrew
Provides:       tex-babel-hebrew = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Hebrew
Version:        svn30273.2.3h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(inputenc.sty), tex(babel.sty)
Provides:       tex(8859-8.def) = %{tl_version}, tex(cp1255.def) = %{tl_version}
Provides:       tex(cp862.def) = %{tl_version}, tex(he8OmegaHebrew.fd) = %{tl_version}
Provides:       tex(he8aharoni.fd) = %{tl_version}, tex(he8cmr.fd) = %{tl_version}
Provides:       tex(he8cmss.fd) = %{tl_version}, tex(he8cmtt.fd) = %{tl_version}
Provides:       tex(he8david.fd) = %{tl_version}, tex(he8drugulin.fd) = %{tl_version}
Provides:       tex(he8enc.def) = %{tl_version}, tex(he8frankruehl.fd) = %{tl_version}
Provides:       tex(he8miriam.fd) = %{tl_version}, tex(he8nachlieli.fd) = %{tl_version}
Provides:       tex(he8yad.fd) = %{tl_version}, tex(hebcal.sty) = %{tl_version}
Provides:       tex(hebfont.sty) = %{tl_version}, tex(hebrew.ldf) = %{tl_version}
Provides:       tex(hebrew_newcode.sty) = %{tl_version}, tex(hebrew_oldcode.sty) = %{tl_version}
Provides:       tex(hebrew_p.sty) = %{tl_version}, tex(lheclas.fd) = %{tl_version}
Provides:       tex(lhecmr.fd) = %{tl_version}, tex(lhecmss.fd) = %{tl_version}
Provides:       tex(lhecmtt.fd) = %{tl_version}, tex(lhecrml.fd) = %{tl_version}
Provides:       tex(lheenc.def) = %{tl_version}, tex(lhefr.fd) = %{tl_version}
Provides:       tex(lheredis.fd) = %{tl_version}, tex(lheshold.fd) = %{tl_version}
Provides:       tex(lheshscr.fd) = %{tl_version}, tex(lheshstk.fd) = %{tl_version}
Provides:       tex(rlbabel.def) = %{tl_version}, tex(si960.def) = %{tl_version}

%description -n texlive-babel-hebrew
The package provides the language definition file for support
of Hebrew in babel. Macros to control the use of text direction
control of TeX--XeT and e-TeX are provided (and may be used
elsewhere). Some shortcuts are defined, as well as translations
to Hebrew of standard "LaTeX names".

%package -n texlive-babel-hebrew-doc
Summary:        Documentation for babel-hebrew
Version:        svn30273.2.3h

Provides:       tex-babel-hebrew-doc
AutoReqProv:    No

%description -n texlive-babel-hebrew-doc
Documentation for babel-hebrew

%package -n texlive-babel-hungarian
Provides:       tex-babel-hungarian = %{tl_version}
License:        LPPL
Summary:        Babel support for Hungarian (Magyar)
Version:        svn45186
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(textcase.sty)
Provides:       tex(magyar.ldf) = %{tl_version}

%description -n texlive-babel-hungarian
The package provides a language definition file that enables
support of Magyar (Hungarian) with babel.

%package -n texlive-babel-hungarian-doc
Summary:        Documentation for babel-hungarian
Version:        svn45186
Provides:       tex-babel-hungarian-doc
AutoReqProv:    No

%description -n texlive-babel-hungarian-doc
Documentation for babel-hungarian

%package -n texlive-babel-icelandic
Provides:       tex-babel-icelandic = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Icelandic
Version:        svn39387

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(icelandic.ldf) = %{tl_version}

%description -n texlive-babel-icelandic
The package provides the language definition file for support
of Icelandic in babel. Some shortcuts are defined, as well as
translations to Icelandic of standard "LaTeX names".

%package -n texlive-babel-icelandic-doc
Summary:        Documentation for babel-icelandic
Version:        svn39387

Provides:       tex-babel-icelandic-doc
AutoReqProv:    No

%description -n texlive-babel-icelandic-doc
Documentation for babel-icelandic

%package -n texlive-babel-interlingua
Provides:       tex-babel-interlingua = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Interlingua
Version:        svn30276.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(interlingua.ldf) = %{tl_version}

%description -n texlive-babel-interlingua
The package provides the language definition file for support
of Interlingua in babel. Translations to Interlingua of
standard "LaTeX names" (no shortcuts are provided). Interlingua
itself is an auxiliary language, built from the common
vocabulary of Spanish/Portuguese, English, Italian and French,
with some normalisation of spelling.

%package -n texlive-babel-interlingua-doc
Summary:        Documentation for babel-interlingua
Version:        svn30276.1.6

Provides:       tex-babel-interlingua-doc
AutoReqProv:    No

%description -n texlive-babel-interlingua-doc
Documentation for babel-interlingua

%package -n texlive-babel-irish
Provides:       tex-babel-irish = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Irish
Version:        svn30277.1.0h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(irish.ldf) = %{tl_version}

%description -n texlive-babel-irish
The package provides the language definition file for support
of Irish Gaelic in babel. The principal content is translations
to Irish of standard "LaTeX names". (No shortcuts are defined.)

%package -n texlive-babel-irish-doc
Summary:        Documentation for babel-irish
Version:        svn30277.1.0h

Provides:       tex-babel-irish-doc
AutoReqProv:    No

%description -n texlive-babel-irish-doc
Documentation for babel-irish

%package -n texlive-babel-italian
Provides:       tex-babel-italian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Italian text
Version:        svn36645.1.3n

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty)
Provides:       tex(italian.ldf) = %{tl_version}

%description -n texlive-babel-italian
The package provides language definitions for use in babel.

%package -n texlive-babel-italian-doc
Summary:        Documentation for babel-italian
Version:        svn36645.1.3n

Provides:       tex-babel-italian-doc
AutoReqProv:    No

%description -n texlive-babel-italian-doc
Documentation for babel-italian

%package -n texlive-babel-kurmanji
Provides:       tex-babel-kurmanji = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Kurmanji
Version:        svn30279.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(kurmanji.ldf) = %{tl_version}

%description -n texlive-babel-kurmanji
The package provides the language definition file for support
of Kurmanji in babel. Kurmanji belongs to the family of Kurdish
languages. Some shortcuts are defined, as well as translations
to Kurmanji of standard "LaTeX names". Note that the package is
dealing with 'Northern' Kurdish, written using a Latin-based
alphabet. The arabxetex package offers support for Kurdish
written in Arabic script.

%package -n texlive-babel-kurmanji-doc
Summary:        Documentation for babel-kurmanji
Version:        svn30279.1.1

Provides:       tex-babel-kurmanji-doc
AutoReqProv:    No

%description -n texlive-babel-kurmanji-doc
Documentation for babel-kurmanji

%package -n texlive-babel-latin
Provides:       tex-babel-latin = %{tl_version}
License:        LPPL
Summary:        Babel support for Latin
Version:        svn38173.3.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ecclesiastic.sty)
Provides:       tex(latin.ldf) = %{tl_version}

%description -n texlive-babel-latin
The package provides the language definition file for support
of Latin in babel. Translations to Latin (in both modern and
medieval spelling) of standard "LaTeX names", and some
shortcuts, are provided. Apart from the modern vs. medieval
setting, a further switch permits addition of prosodic marks.

%package -n texlive-babel-latin-doc
Summary:        Documentation for babel-latin
Version:        svn38173.3.5

Provides:       tex-babel-latin-doc
AutoReqProv:    No

%description -n texlive-babel-latin-doc
Documentation for babel-latin

%package -n texlive-babel-latvian
Provides:       tex-babel-latvian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Latvian
Version:        svn46681
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(latvian.ldf) = %{tl_version}

%description -n texlive-babel-latvian
The package provides the language definition file for support
of Latvian in babel.

%package -n texlive-babel-latvian-doc
Summary:        Documentation for babel-latvian
Version:        svn46681
Provides:       tex-babel-latvian-doc
AutoReqProv:    No

%description -n texlive-babel-latvian-doc
Documentation for babel-latvian

%package -n texlive-babel-norsk
Provides:       tex-babel-norsk = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Norwegian
Version:        svn30281.2.0i

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(norsk.ldf) = %{tl_version}

%description -n texlive-babel-norsk
The package provides the language definition file for support
of Norwegian in babel. Some shortcuts are defined, as well as
translations to Norsk of standard "LaTeX names".

%package -n texlive-babel-norsk-doc
Summary:        Documentation for babel-norsk
Version:        svn30281.2.0i

Provides:       tex-babel-norsk-doc
AutoReqProv:    No

%description -n texlive-babel-norsk-doc
Documentation for babel-norsk

%package -n texlive-babel-piedmontese
Provides:       tex-babel-piedmontese = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Piedmontese
Version:        svn30282.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(piedmontese.ldf) = %{tl_version}

%description -n texlive-babel-piedmontese
The package provides the language definition file for support
of Piedmontese in babel. Some shortcuts are defined, as well as
translations to Piedmontese of standard "LaTeX names".

%package -n texlive-babel-piedmontese-doc
Summary:        Documentation for babel-piedmontese
Version:        svn30282.1.0

Provides:       tex-babel-piedmontese-doc
AutoReqProv:    No

%description -n texlive-babel-piedmontese-doc
Documentation for babel-piedmontese

%package -n texlive-babel-polish
Provides:       tex-babel-polish = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Polish
Version:        svn30283.1.2l

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(polish.ldf) = %{tl_version}

%description -n texlive-babel-polish
The package provides the language definition file for support
of Polish in babel. Some shortcuts are defined, as well as
translations to Polish of standard "LaTeX names".

%package -n texlive-babel-polish-doc
Summary:        Documentation for babel-polish
Version:        svn30283.1.2l

Provides:       tex-babel-polish-doc
AutoReqProv:    No

%description -n texlive-babel-polish-doc
Documentation for babel-polish

%package -n texlive-babel-portuges
Provides:       tex-babel-portuges = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Portuges
Version:        svn30284.1.2q

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(portuges.ldf) = %{tl_version}

%description -n texlive-babel-portuges
The package provides the language definition file for support
of Portuguese and Brazilian Portuguese in babel. Some shortcuts
are defined, as well as translations to Portuguese of standard
"LaTeX names".

%package -n texlive-babel-portuges-doc
Summary:        Documentation for babel-portuges
Version:        svn30284.1.2q

Provides:       tex-babel-portuges-doc
AutoReqProv:    No

%description -n texlive-babel-portuges-doc
Documentation for babel-portuges

%package -n texlive-babel-romanian
Provides:       tex-babel-romanian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Romanian
Version:        svn30285.1.2l

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(romanian.ldf) = %{tl_version}

%description -n texlive-babel-romanian
The package provides the language definition file for support
of Romanian in babel. Translations to Romanian of standard
"LaTeX names" are provided.

%package -n texlive-babel-romanian-doc
Summary:        Documentation for babel-romanian
Version:        svn30285.1.2l

Provides:       tex-babel-romanian-doc
AutoReqProv:    No

%description -n texlive-babel-romanian-doc
Documentation for babel-romanian

%package -n texlive-babel-romansh
Provides:       tex-babel-romansh = %{tl_version}
License:        LPPL 1.3
Summary:        Babel/Polyglossia support for the Romansh language
Version:        svn30286.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(romansh.ldf) = %{tl_version}

%description -n texlive-babel-romansh
The package provides a language description file that enables
support of Romansh either with babel or with polyglossia.

%package -n texlive-babel-romansh-doc
Summary:        Documentation for babel-romansh
Version:        svn30286.0

Provides:       tex-babel-romansh-doc
AutoReqProv:    No

%description -n texlive-babel-romansh-doc
Documentation for babel-romansh

%package -n texlive-babel-russian
Provides:       tex-babel-russian = %{tl_version}
License:        LPPL 1.3
Summary:        Russian language module for Babel
Version:        svn45007
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(russianb.ldf) = %{tl_version}

%description -n texlive-babel-russian
The package provides support for use of Babel in documents
written in Russian (in both "traditional" and modern forms).
The support is adapted for use both under 'traditional' TeX
engines, and under XeTeX and LuaTeX.

%package -n texlive-babel-russian-doc
Summary:        Documentation for babel-russian
Version:        svn45007
Provides:       tex-babel-russian-doc
AutoReqProv:    No

%description -n texlive-babel-russian-doc
Documentation for babel-russian

%package -n texlive-babel-samin
Provides:       tex-babel-samin = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Samin
Version:        svn30288.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(samin.ldf) = %{tl_version}

%description -n texlive-babel-samin
The package provides the language definition file for support
of North Sami in babel. (Several Sami dialects/languages are
spoken in Finland, Norway, Sweden and on the Kola Peninsula of
Russia). Not all use the same alphabet, and no attempt is made
to support any other than North Sami here. Some shortcuts are
defined, as well as translations to Norsk of standard "LaTeX
names".

%package -n texlive-babel-samin-doc
Summary:        Documentation for babel-samin
Version:        svn30288.1.0c

Provides:       tex-babel-samin-doc
AutoReqProv:    No

%description -n texlive-babel-samin-doc
Documentation for babel-samin

%package -n texlive-babel-scottish
Provides:       tex-babel-scottish = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Scottish Gaelic
Version:        svn30289.1.0g

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(scottish.ldf) = %{tl_version}

%description -n texlive-babel-scottish
The package provides the language definition file for support
of Gaidhlig (Scottish Gaelic) in babel. Some shortcuts are
defined, as well as translations of standard "LaTeX names".

%package -n texlive-babel-scottish-doc
Summary:        Documentation for babel-scottish
Version:        svn30289.1.0g

Provides:       tex-babel-scottish-doc
AutoReqProv:    No

%description -n texlive-babel-scottish-doc
Documentation for babel-scottish

%package -n texlive-babel-serbianc
Provides:       tex-babel-serbianc = %{tl_version}
License:        LPPL 1.3
Summary:        Babel module to support Serbian Cyrillic
Version:        svn30348.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ucs.sty), tex(inputenc.sty), tex(fontenc.sty)
Provides:       tex(serbianc.ldf) = %{tl_version}, tex(serbianc.sty) = %{tl_version}

%description -n texlive-babel-serbianc
The package provides support for Serbian documents written in
Cyrillic, in babel.

%package -n texlive-babel-serbianc-doc
Summary:        Documentation for babel-serbianc
Version:        svn30348.2.2

Provides:       tex-babel-serbianc-doc
AutoReqProv:    No

%description -n texlive-babel-serbianc-doc
Documentation for babel-serbianc

%package -n texlive-babel-serbian
Provides:       tex-babel-serbian = %{tl_version}
License:        LPPL
Summary:        babel-serbian package
Version:        svn30290.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(serbian.ldf) = %{tl_version}

%description -n texlive-babel-serbian
babel-serbian package

%package -n texlive-babel-serbian-doc
Summary:        Documentation for babel-serbian
Version:        svn30290.0

Provides:       tex-babel-serbian-doc
AutoReqProv:    No

%description -n texlive-babel-serbian-doc
Documentation for babel-serbian

%package -n texlive-babel-slovak
Provides:       tex-babel-slovak = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for typesetting Slovak
Version:        svn30292.3.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(slovak.ldf) = %{tl_version}, tex(slovak.sty) = %{tl_version}

%description -n texlive-babel-slovak
The package provides the language definition file for support
of Slovak in babel, including Slovak variants of LaTeX built-in-
names. Shortcuts are also defined.

%package -n texlive-babel-slovak-doc
Summary:        Documentation for babel-slovak
Version:        svn30292.3.1a

Provides:       tex-babel-slovak-doc
AutoReqProv:    No

%description -n texlive-babel-slovak-doc
Documentation for babel-slovak

%package -n texlive-babel-slovenian
Provides:       tex-babel-slovenian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for typesetting Slovenian
Version:        svn30351.1.2i

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(slovene.ldf) = %{tl_version}

%description -n texlive-babel-slovenian
The package provides the language definition file for support
of Slovenian in babel. Several shortcuts are defined, as well
as translations to Slovenian of standard "LaTeX names".

%package -n texlive-babel-slovenian-doc
Summary:        Documentation for babel-slovenian
Version:        svn30351.1.2i

Provides:       tex-babel-slovenian-doc
AutoReqProv:    No

%description -n texlive-babel-slovenian-doc
Documentation for babel-slovenian

%package -n texlive-babel-sorbian
Provides:       tex-babel-sorbian = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Upper and Lower Sorbian
Version:        svn30294

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lsorbian.ldf) = %{tl_version}, tex(usorbian.ldf) = %{tl_version}

%description -n texlive-babel-sorbian
The package provides language definitions file for support of
both Upper and Lower Sorbian, in babel. Some shortcuts are
defined, as well as translations to the relevant language of
standard "LaTeX names".

%package -n texlive-babel-sorbian-doc
Summary:        Documentation for babel-sorbian
Version:        svn30294

Provides:       tex-babel-sorbian-doc
AutoReqProv:    No

%description -n texlive-babel-sorbian-doc
Documentation for babel-sorbian

%package -n texlive-babel-spanglish
Provides:       tex-babel-spanglish = %{tl_version}
License:        LPPL 1.3
Summary:        Simplified Spanish support for Babel
Version:        svn37629.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(spanglish.ldf) = %{tl_version}, tex(spanglish.sty) = %{tl_version}

%description -n texlive-babel-spanglish
The package provides very simplified (or ultra sloppy) support
for Spanish in Babel, mostly as a fallback in case spanish.ldf
fails for some reason. The package provides basic support for
Spanish hyphenation, captions, date, frenchspacing,
indentfirst, symbolic footnotes, enumerations, small caps roman
numerals, and a handful of shorthands and Spanish mathematical
operators. No options or attributes for customization are
provided.

%package -n texlive-babel-spanglish-doc
Summary:        Documentation for babel-spanglish
Version:        svn37629.0.3

Provides:       tex-babel-spanglish-doc
AutoReqProv:    No

%description -n texlive-babel-spanglish-doc
Documentation for babel-spanglish

%package -n texlive-babel-spanish
Provides:       tex-babel-spanish = %{tl_version}
License:        LPPL
Summary:        Babel support for Spanish
Version:        svn39920

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(romanidx.sty) = %{tl_version}, tex(spanish.ldf) = %{tl_version}

%description -n texlive-babel-spanish
This bundle provides the means to typeset Spanish text, with
the support provided by the LaTeX standard package babel. Note
that separate support is provided for those who wish to typeset
Spanish as written in Mexico.

%package -n texlive-babel-spanish-doc
Summary:        Documentation for babel-spanish
Version:        svn39920

Provides:       tex-babel-spanish-doc
AutoReqProv:    No

%description -n texlive-babel-spanish-doc
Documentation for babel-spanish

%package -n texlive-babel-swedish
Provides:       tex-babel-swedish = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for typesetting Swedish
Version:        svn30296.2.3d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(swedish.ldf) = %{tl_version}

%description -n texlive-babel-swedish
The package provides the language definition file for Swedish.

%package -n texlive-babel-swedish-doc
Summary:        Documentation for babel-swedish
Version:        svn30296.2.3d

Provides:       tex-babel-swedish-doc
AutoReqProv:    No

%description -n texlive-babel-swedish-doc
Documentation for babel-swedish

%package -n texlive-babel-thai
Provides:       tex-babel-thai = %{tl_version}
License:        LPPL 1.3
Summary:        Support for Thai within babel
Version:        svn30564.1.0.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(lthenc.def) = %{tl_version}, tex(thai.ldf) = %{tl_version}
Provides:       tex(tis620.def) = %{tl_version}

%description -n texlive-babel-thai
The package provides support for typesetting Thai text. within
the babel system.

%package -n texlive-babel-thai-doc
Summary:        Documentation for babel-thai
Version:        svn30564.1.0.0

Provides:       tex-babel-thai-doc
AutoReqProv:    No

%description -n texlive-babel-thai-doc
Documentation for babel-thai

%package -n texlive-babel
Provides:       tex-babel = %{tl_version}
License:        LPPL 1.3
Summary:        Multilingual support for Plain TeX or LaTeX
Version:        svn47932
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(UKenglish.sty) = %{tl_version}, tex(USenglish.sty) = %{tl_version}
Provides:       tex(afrikaans.sty) = %{tl_version}, tex(albanian.sty) = %{tl_version}
Provides:       tex(american.sty) = %{tl_version}, tex(austrian.sty) = %{tl_version}
Provides:       tex(babel.def) = %{tl_version}, tex(babel.sty) = %{tl_version}
Provides:       tex(bahasa.sty) = %{tl_version}, tex(bahasam.sty) = %{tl_version}
Provides:       tex(basque.sty) = %{tl_version}, tex(blplain.tex) = %{tl_version}
Provides:       tex(bplain.tex) = %{tl_version}, tex(breton.sty) = %{tl_version}
Provides:       tex(british.sty) = %{tl_version}, tex(bulgarian.sty) = %{tl_version}
Provides:       tex(catalan.sty) = %{tl_version}, tex(croatian.sty) = %{tl_version}
Provides:       tex(czech.sty) = %{tl_version}, tex(danish.sty) = %{tl_version}
Provides:       tex(dutch.sty) = %{tl_version}, tex(english.sty) = %{tl_version}
Provides:       tex(esperanto.sty) = %{tl_version}, tex(estonian.sty) = %{tl_version}
Provides:       tex(finnish.sty) = %{tl_version}, tex(francais.sty) = %{tl_version}
Provides:       tex(galician.sty) = %{tl_version}, tex(germanb.sty) = %{tl_version}
Provides:       tex(greek.sty) = %{tl_version}, tex(hebrew.sty) = %{tl_version}
Provides:       tex(hyphen.cfg) = %{tl_version}, tex(icelandic.sty) = %{tl_version}
Provides:       tex(interlingua.sty) = %{tl_version}, tex(irish.sty) = %{tl_version}
Provides:       tex(italian.sty) = %{tl_version}, tex(latin.sty) = %{tl_version}
Provides:       tex(lsorbian.sty) = %{tl_version}, tex(luababel.def) = %{tl_version}
Provides:       tex(magyar.sty) = %{tl_version}, tex(naustrian.sty) = %{tl_version}
Provides:       tex(ngermanb.sty) = %{tl_version}, tex(nil.ldf) = %{tl_version}
Provides:       tex(norsk.sty) = %{tl_version}, tex(plain.def) = %{tl_version}
Provides:       tex(polish.sty) = %{tl_version}, tex(portuges.sty) = %{tl_version}
Provides:       tex(romanian.sty) = %{tl_version}, tex(russianb.sty) = %{tl_version}
Provides:       tex(samin.sty) = %{tl_version}, tex(scottish.sty) = %{tl_version}
Provides:       tex(serbian.sty) = %{tl_version}, tex(slovak.sty) = %{tl_version}
Provides:       tex(slovene.sty) = %{tl_version}, tex(spanish.sty) = %{tl_version}
Provides:       tex(swedish.sty) = %{tl_version}, tex(switch.def) = %{tl_version}
Provides:       tex(turkish.sty) = %{tl_version}, tex(ukraineb.sty) = %{tl_version}
Provides:       tex(usorbian.sty) = %{tl_version}, tex(welsh.sty) = %{tl_version}
Provides:       tex(xebabel.def) = %{tl_version}

%description -n texlive-babel
The package manages culturally-determined typographical (and
other) rules, and hyphenation patterns for a wide range of
languages. A document may select a single language to be
supported, or it may select several, in which case the document
may switch from one language to another in a variety of ways.
Babel uses contributed configuration files that provide the
detail of what has to be done for each language. Users of XeTeX
are advised to use polyglossia rather than Babel.

%package -n texlive-babel-doc
Summary:        Documentation for babel
Version:        svn47932
Provides:       tex-babel-doc
AutoReqProv:    No

%description -n texlive-babel-doc
Documentation for babel

%package -n texlive-babel-turkish
Provides:       tex-babel-turkish = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Turkish documents
Version:        svn33284.1.3b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(turkish.ldf) = %{tl_version}

%description -n texlive-babel-turkish
The package provides support, within babel, of the Turkish
language.

%package -n texlive-babel-turkish-doc
Summary:        Documentation for babel-turkish
Version:        svn33284.1.3b

Provides:       tex-babel-turkish-doc
AutoReqProv:    No

%description -n texlive-babel-turkish-doc
Documentation for babel-turkish

%package -n texlive-babel-ukrainian
Provides:       babel-ukraineb = %{tl_version}
Obsoletes:      babel-ukraineb < 2016
Provides:       tex-babel-ukrainian = %{tl_version}, tex-babel-ukraineb = %{tl_version}
License:        LPPL
Summary:        babel-ukrainian package
Version:        svn47585
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(ukraineb.ldf) = %{tl_version}

%description -n texlive-babel-ukrainian
babel-ukrainian package

%package -n texlive-babel-ukrainian-doc
Summary:        Documentation for babel-ukrainian
Version:        svn47585
Provides:       tex-babel-ukrainian-doc = %{tl_version}
Obsoletes:      babel-ukraineb-doc < 2016
Provides:       tex-babel-ukraineb-doc
AutoReqProv:    No

%description -n texlive-babel-ukrainian-doc
Documentation for babel-ukrainian

%package -n texlive-babel-vietnamese
Provides:       tex-babel-vietnamese = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for typesetting Vietnamese
Version:        svn39246

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(vncaps.tex), tex(vncaps.tex)
Provides:       tex(vietnam.ldf) = %{tl_version}, tex(vietnamese.ldf) = %{tl_version}

%description -n texlive-babel-vietnamese
The package provides the language definition file for support
of Vietnamese in babel.

%package -n texlive-babel-welsh
Provides:       tex-babel-welsh = %{tl_version}
License:        LPPL 1.3
Summary:        Babel support for Welsh
Version:        svn38372.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(welsh.ldf) = %{tl_version}

%description -n texlive-babel-welsh
The package provides the language definition file for Welsh.
(Mostly Welsh-language versions of the standard names in a
LaTeX file.)

%package -n texlive-babel-welsh-doc
Summary:        Documentation for babel-welsh
Version:        svn38372.1.1a

Provides:       tex-babel-welsh-doc
AutoReqProv:    No

%description -n texlive-babel-welsh-doc
Documentation for babel-welsh

%package -n texlive-background
Provides:       tex-background = %{tl_version}
License:        LPPL
Summary:        Placement of background material on pages of a document
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(tikz.sty), tex(everypage.sty), tex(afterpage.sty)
Provides:       tex(background.sty) = %{tl_version}

%description -n texlive-background
The package offers the placement of background material on the
pages of a document. The user can control many aspects
(contents, position, color, opacity) of the background material
that will be displayed; all placement and attribute settings
are controlled by setting key values. The package makes use of
the everypage package, and uses pgf/tikz for attribute control.

%package -n texlive-background-doc
Summary:        Documentation for background
Version:        svn42428
Provides:       tex-background-doc
AutoReqProv:    No

%description -n texlive-background-doc
Documentation for background

%package -n texlive-backnaur
Provides:       tex-backnaur = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Backus Naur Form definitions
Version:        svn28513.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(backnaur.sty) = %{tl_version}

%description -n texlive-backnaur
The package typesets Backus-Naur Form (BNF) definitions. It
creates aligned lists of productions, with numbers if required.
It can also print in-line BNF expressions using math mode.

%package -n texlive-backnaur-doc
Summary:        Documentation for backnaur
Version:        svn28513.1.1

Provides:       tex-backnaur-doc
AutoReqProv:    No

%description -n texlive-backnaur-doc
Documentation for backnaur

%package -n texlive-bagpipe
Provides:       tex-bagpipe = %{tl_version}
License:        LPPL 1.3
Summary:        Support for typesetting bagpipe music
Version:        svn34393.3.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bagpipe.tex) = %{tl_version}

%description -n texlive-bagpipe
Typesetting bagpipe music in MusixTeX is needlessly tedious.
This package provides specialized and re-defined macros to
simplify this task.

%package -n texlive-bagpipe-doc
Summary:        Documentation for bagpipe
Version:        svn34393.3.02

Provides:       tex-bagpipe-doc
AutoReqProv:    No

%description -n texlive-bagpipe-doc
Documentation for bagpipe

%package -n texlive-bangorcsthesis
Provides:       tex-bangorcsthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset a thesis at Bangor University
Version:        svn45059
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fifo-stack.sty), tex(ifthen.sty), tex(xkeyval.sty), tex(xcolor.sty)
Requires:       tex(draftwatermark.sty), tex(fontenc.sty)
Requires:       tex(babel.sty), tex(isodate.sty), tex(inputenc.sty), tex(xparse.sty)
Requires:       tex(parskip.sty), tex(indentfirst.sty), tex(berasans.sty), tex(charter.sty)
Requires:       tex(graphicx.sty), tex(url.sty), tex(csquotes.sty), tex(fixltx2e.sty)
Requires:       tex(microtype.sty), tex(setspace.sty), tex(fancyhdr.sty), tex(enumitem.sty)
Requires:       tex(amsmath.sty), tex(hyperref.sty), tex(cleveref.sty), tex(geometry.sty)
Requires:       tex(biblatex.sty), tex(caption.sty), tex(titlesec.sty), tex(tocloft.sty)
Requires:       tex(tikz.sty), tex(forloop.sty), tex(framed.sty), tex(totalcount.sty)
Provides:       tex(bangorcsthesis.cls) = %{tl_version}

%description -n texlive-bangorcsthesis
The class typesets thesis/dissertation documents for all levels
(i.e., both undergraduate and graduate students may use the
class). It also provides macros designed to optimise the
process of producing a thesis.

%package -n texlive-bangorcsthesis-doc
Summary:        Documentation for bangorcsthesis
Version:        svn45059
Provides:       tex-bangorcsthesis-doc
AutoReqProv:    No

%description -n texlive-bangorcsthesis-doc
Documentation for bangorcsthesis

%package -n texlive-bangtex
Provides:       tex-bangtex = %{tl_version}
License:        LPPL
Summary:        Writing Bangla and Assamese with LaTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bang10.tfm) = %{tl_version}, tex(bangsl10.tfm) = %{tl_version}
Provides:       tex(bangwd10.tfm) = %{tl_version}, tex(bangfont.tex) = %{tl_version}
Provides:       tex(barticle.cls) = %{tl_version}, tex(bbk10.clo) = %{tl_version}
Provides:       tex(bbk11.clo) = %{tl_version}, tex(bbk12.clo) = %{tl_version}
Provides:       tex(bbook.cls) = %{tl_version}, tex(bletter.cls) = %{tl_version}
Provides:       tex(bsize10.clo) = %{tl_version}, tex(bsize11.clo) = %{tl_version}
Provides:       tex(bsize12.clo) = %{tl_version}

%description -n texlive-bangtex
The bundle provides class files for writing Bangla and Assamese
with LaTeX, and Metafont sources for fonts.

%package -n texlive-bangtex-doc
Summary:        Documentation for bangtex
Version:        svn15878.0

Provides:       tex-bangtex-doc
AutoReqProv:    No

%description -n texlive-bangtex-doc
Documentation for bangtex

%package -n texlive-bankstatement
Provides:       tex-bankstatement = %{tl_version}
License:        LPPL
Summary:        A LaTeX class for bank statements based on csv data
Version:        svn38857

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(xkvltxp.sty), tex(geometry.sty), tex(longtable.sty)
Requires:       tex(tabularx.sty), tex(xcolor.sty), tex(graphicx.sty), tex(booktabs.sty)
Requires:       tex(datatool.sty), tex(calc.sty), tex(ifthen.sty)
Provides:       tex(bankstatement.cls) = %{tl_version}, tex(csv-camt.def) = %{tl_version}
Provides:       tex(csv-mt940.def) = %{tl_version}, tex(stmenglish.def) = %{tl_version}
Provides:       tex(stmgerman.def) = %{tl_version}

%description -n texlive-bankstatement
More and more banks allow their customers to download posting
records in various formats. By using the bankstatement class,
you can create bank statements, as long as a csv format is
available. At the moment, the csv-mt940 and csv-camt formats --
used by many german Sparkassen -- are supported. You can quite
easily add support for other csv formats. Simply define the
order of the keys in the csv data file and how to use them. The
terminology in this class -- such as BIC (Business Identifier
Code) or IBAN (International Bank Account Number) -- is based
on usage in the SEPA (Single Euro Payments Area). The user may
adjust the terminology to suit local needs.

%package -n texlive-bankstatement-doc
Summary:        Documentation for bankstatement
Version:        svn38857

Provides:       tex-bankstatement-doc
AutoReqProv:    No

%description -n texlive-bankstatement-doc
Documentation for bankstatement

%package -n texlive-barcodes
Provides:       tex-barcodes = %{tl_version}
License:        LPPL
Summary:        Fonts for making barcodes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(wlc11.tfm) = %{tl_version}, tex(wlc128.tfm) = %{tl_version}
Provides:       tex(wlc39.tfm) = %{tl_version}, tex(wlc93.tfm) = %{tl_version}
Provides:       tex(wlcr39.tfm) = %{tl_version}, tex(barcodes.sty) = %{tl_version}

%description -n texlive-barcodes
The package deals with EAN barcodes; Metafont sources for fonts
are provided, and a set of examples; for some codes, a small
Perl script is needed.

%package -n texlive-barcodes-doc
Summary:        Documentation for barcodes
Version:        svn15878.0

Provides:       tex-barcodes-doc
AutoReqProv:    No

%description -n texlive-barcodes-doc
Documentation for barcodes

%package -n texlive-bardiag
Provides:       tex-bardiag = %{tl_version}
License:        LPPL
Summary:        LateX package for drawing bar diagrams
Version:        svn22013.0.4a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(fp-snap.sty), tex(pstricks.sty), tex(pstcol.sty)
Requires:       tex(pst-grad.sty), tex(multido.sty), tex(ifthen.sty)
Provides:       tex(barddoc.sty) = %{tl_version}, tex(bardiag.cfg) = %{tl_version}
Provides:       tex(bardiag.sty) = %{tl_version}, tex(pstfp.sty) = %{tl_version}

%description -n texlive-bardiag
The main purpose of the package is to make the drawing of bar
diagrams possible and easy in LaTeX. The BarDiag package is
inspired by and based on PSTricks.

%package -n texlive-bardiag-doc
Summary:        Documentation for bardiag
Version:        svn22013.0.4a

Provides:       tex-bardiag-doc
AutoReqProv:    No

%description -n texlive-bardiag-doc
Documentation for bardiag

%package -n texlive-barr
Provides:       tex-barr = %{tl_version}
License:        LPPL
Summary:        Diagram macros by Michael Barr
Version:        svn38479

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(diagxy.tex) = %{tl_version}

%description -n texlive-barr
Diagxy is a general diagramming package, useful for diagrams in
a number of mathematical disciplines. Diagxy is a development
of an earlier (successful) package to use the facilities of the
xypic bundle.

%package -n texlive-barr-doc
Summary:        Documentation for barr
Version:        svn38479

Provides:       tex-barr-doc
AutoReqProv:    No

%description -n texlive-barr-doc
Documentation for barr

%package -n texlive-bartel-chess-fonts
Provides:       tex-bartel-chess-fonts = %{tl_version}
License:        GPL+
Summary:        A set of fonts supporting chess diagrams
Version:        svn20619.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(fselch10.tfm) = %{tl_version}, tex(fselch11.tfm) = %{tl_version}
Provides:       tex(fselch12.tfm) = %{tl_version}, tex(fselch13.tfm) = %{tl_version}
Provides:       tex(fselch14.tfm) = %{tl_version}, tex(fselch16.tfm) = %{tl_version}
Provides:       tex(fselch17.tfm) = %{tl_version}, tex(fselch20.tfm) = %{tl_version}
Provides:       tex(fselch24.tfm) = %{tl_version}, tex(fselch32.tfm) = %{tl_version}
Provides:       tex(fselch36.tfm) = %{tl_version}, tex(fselch6.tfm) = %{tl_version}
Provides:       tex(fselch7.tfm) = %{tl_version}, tex(fselch8.tfm) = %{tl_version}
Provides:       tex(fselch9.tfm) = %{tl_version}, tex(pkelch10.tfm) = %{tl_version}
Provides:       tex(pkelch11.tfm) = %{tl_version}, tex(pkelch12.tfm) = %{tl_version}
Provides:       tex(pkelch14.tfm) = %{tl_version}, tex(pkelch16.tfm) = %{tl_version}
Provides:       tex(pkelch8.tfm) = %{tl_version}, tex(pkelch9.tfm) = %{tl_version}

%description -n texlive-bartel-chess-fonts
The fonts are provided as Metafont source.

%package -n texlive-bartel-chess-fonts-doc
Summary:        Documentation for bartel-chess-fonts
Version:        svn20619.0

Provides:       tex-bartel-chess-fonts-doc
AutoReqProv:    No

%description -n texlive-bartel-chess-fonts-doc
Documentation for bartel-chess-fonts

%package -n texlive-bashful
Provides:       tex-bashful = %{tl_version}
License:        LPPL 1.3
Summary:        Invoke bash commands from within LaTeX
Version:        svn25597.0.93

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty), tex(catchfile.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(listings.sty)
Provides:       tex(bashful.sty) = %{tl_version}

%description -n texlive-bashful
The package makes it possible to execute Unix bash shell
scripts from within LaTeX. The main application is in writing
computer-science texts, in which you want to make sure the
programs listed in the document are executed directly from the
input. The package may use other Unix shells than bash, but
does not work without modification in a Windows environment.
The package requires the -shell-escape flag when LaTeX is
processing your document.

%package -n texlive-bashful-doc
Summary:        Documentation for bashful
Version:        svn25597.0.93

Provides:       tex-bashful-doc
AutoReqProv:    No

%description -n texlive-bashful-doc
Documentation for bashful

%package -n texlive-basicarith
Provides:       tex-basicarith = %{tl_version}
License:        LPPL 1.3
Summary:        Macros for typesetting basic arithmetic
Version:        svn35460.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(basicarith.sty) = %{tl_version}

%description -n texlive-basicarith
The package provides macros for typesetting basic arithmetic,
in the style typically found in textbooks. It focuses on the
American style of performing these algorithms. It is written
mostly in low-level TeX, with the goal that it should run in
either plain TeX or LaTeX, but there are two constructions that
currently prevent this. It is highly configurable, with macros
and lengths described in the documentation.

%package -n texlive-basicarith-doc
Summary:        Documentation for basicarith
Version:        svn35460.1.1

Provides:       tex-basicarith-doc
AutoReqProv:    No

%description -n texlive-basicarith-doc
Documentation for basicarith

%package -n texlive-baskervald
Provides:       tex-baskervald = %{tl_version}
License:        LPPL
Summary:        Baskervald ADF fonts collection with TeX/LaTeX support
Version:        svn19490.1.016

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(textcomp.sty), tex(nfssext-cfr.sty)
Provides:       tex(supp-ybv.enc) = %{tl_version}, tex(ybv.map) = %{tl_version}
Provides:       tex(ybvb8c.tfm) = %{tl_version}, tex(ybvb8r.tfm) = %{tl_version}
Provides:       tex(ybvb8s.tfm) = %{tl_version}, tex(ybvb8t.tfm) = %{tl_version}
Provides:       tex(ybvbi8c.tfm) = %{tl_version}, tex(ybvbi8r.tfm) = %{tl_version}
Provides:       tex(ybvbi8s.tfm) = %{tl_version}, tex(ybvbi8t.tfm) = %{tl_version}
Provides:       tex(ybvbiw8t.tfm) = %{tl_version}, tex(ybvbw8t.tfm) = %{tl_version}
Provides:       tex(ybvh8c.tfm) = %{tl_version}, tex(ybvh8r.tfm) = %{tl_version}
Provides:       tex(ybvh8s.tfm) = %{tl_version}, tex(ybvh8t.tfm) = %{tl_version}
Provides:       tex(ybvho8c.tfm) = %{tl_version}, tex(ybvho8r.tfm) = %{tl_version}
Provides:       tex(ybvho8s.tfm) = %{tl_version}, tex(ybvho8t.tfm) = %{tl_version}
Provides:       tex(ybvhow8t.tfm) = %{tl_version}, tex(ybvhw8t.tfm) = %{tl_version}
Provides:       tex(ybvr8c.tfm) = %{tl_version}, tex(ybvr8r.tfm) = %{tl_version}
Provides:       tex(ybvr8s.tfm) = %{tl_version}, tex(ybvr8t.tfm) = %{tl_version}
Provides:       tex(ybvri8c.tfm) = %{tl_version}, tex(ybvri8r.tfm) = %{tl_version}
Provides:       tex(ybvri8s.tfm) = %{tl_version}, tex(ybvri8t.tfm) = %{tl_version}
Provides:       tex(ybvriw8t.tfm) = %{tl_version}, tex(ybvrw8t.tfm) = %{tl_version}
Provides:       tex(ybvb8a.pfb) = %{tl_version}, tex(ybvbi8a.pfb) = %{tl_version}
Provides:       tex(ybvh8a.pfb) = %{tl_version}, tex(ybvho8a.pfb) = %{tl_version}
Provides:       tex(ybvr8a.pfb) = %{tl_version}, tex(ybvri8a.pfb) = %{tl_version}
Provides:       tex(ybvb8c.vf) = %{tl_version}, tex(ybvb8t.vf) = %{tl_version}
Provides:       tex(ybvbi8c.vf) = %{tl_version}, tex(ybvbi8t.vf) = %{tl_version}
Provides:       tex(ybvbiw8t.vf) = %{tl_version}, tex(ybvbw8t.vf) = %{tl_version}
Provides:       tex(ybvh8c.vf) = %{tl_version}, tex(ybvh8t.vf) = %{tl_version}
Provides:       tex(ybvho8c.vf) = %{tl_version}, tex(ybvho8t.vf) = %{tl_version}
Provides:       tex(ybvhow8t.vf) = %{tl_version}, tex(ybvhw8t.vf) = %{tl_version}
Provides:       tex(ybvr8c.vf) = %{tl_version}, tex(ybvr8t.vf) = %{tl_version}
Provides:       tex(ybvri8c.vf) = %{tl_version}, tex(ybvri8t.vf) = %{tl_version}
Provides:       tex(ybvriw8t.vf) = %{tl_version}, tex(ybvrw8t.vf) = %{tl_version}
Provides:       tex(baskervald.sty) = %{tl_version}, tex(t1ybv.fd) = %{tl_version}
Provides:       tex(t1ybvw.fd) = %{tl_version}, tex(ts1ybv.fd) = %{tl_version}
Provides:       tex(ts1ybvw.fd) = %{tl_version}

%description -n texlive-baskervald
Baskervald ADF is a serif family with lining figures designed
as a substitute for Baskerville. The family currently includes
upright and italic or oblique shapes in each of regular, bold
and heavy weights. All fonts include the slashed zero and
additional non-standard ligatures. The support package renames
them according to the Karl Berry fontname scheme and defines
two families. One of these primarily provides access to the
"standard" or default characters while the other supports
additional ligatures. The included package files provide access
to these features in LaTeX.

%package -n texlive-baskervald-doc
Summary:        Documentation for baskervald
Version:        svn19490.1.016

Provides:       tex-baskervald-doc
AutoReqProv:    No

%description -n texlive-baskervald-doc
Documentation for baskervald

%package -n texlive-baskervaldx
Provides:       tex-baskervaldx = %{tl_version}
License:        GPL+
Summary:        Extension and modification of BaskervaldADF with LaTeX support
Version:        svn43461
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(mweights.sty), tex(etoolbox.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(bvalph.enc) = %{tl_version}, tex(bvtabosf.enc) = %{tl_version}
Provides:       tex(zbv_2bp5ef.enc) = %{tl_version}, tex(zbv_2n2qka.enc) = %{tl_version}
Provides:       tex(zbv_2sm4i7.enc) = %{tl_version}, tex(zbv_3lvabu.enc) = %{tl_version}
Provides:       tex(zbv_3omoui.enc) = %{tl_version}, tex(zbv_4f5bev.enc) = %{tl_version}
Provides:       tex(zbv_4kmser.enc) = %{tl_version}, tex(zbv_4ksy5y.enc) = %{tl_version}
Provides:       tex(zbv_537kn6.enc) = %{tl_version}, tex(zbv_5zt4ml.enc) = %{tl_version}
Provides:       tex(zbv_67xtiz.enc) = %{tl_version}, tex(zbv_6mioll.enc) = %{tl_version}
Provides:       tex(zbv_6rdtju.enc) = %{tl_version}, tex(zbv_6rwo65.enc) = %{tl_version}
Provides:       tex(zbv_6tdhgo.enc) = %{tl_version}, tex(zbv_7453eo.enc) = %{tl_version}
Provides:       tex(zbv_7nnme4.enc) = %{tl_version}, tex(zbv_7qmldf.enc) = %{tl_version}
Provides:       tex(zbv_awcfcx.enc) = %{tl_version}, tex(zbv_bgypte.enc) = %{tl_version}
Provides:       tex(zbv_bs5d7e.enc) = %{tl_version}, tex(zbv_caye23.enc) = %{tl_version}
Provides:       tex(zbv_cgzxx6.enc) = %{tl_version}, tex(zbv_ck4t6h.enc) = %{tl_version}
Provides:       tex(zbv_coqtyh.enc) = %{tl_version}, tex(zbv_e3qxqg.enc) = %{tl_version}
Provides:       tex(zbv_ea64ih.enc) = %{tl_version}, tex(zbv_gar3zb.enc) = %{tl_version}
Provides:       tex(zbv_gjwmpg.enc) = %{tl_version}, tex(zbv_go57dj.enc) = %{tl_version}
Provides:       tex(zbv_gsgxts.enc) = %{tl_version}, tex(zbv_h4nqsn.enc) = %{tl_version}
Provides:       tex(zbv_hg6ru4.enc) = %{tl_version}, tex(zbv_hkyy53.enc) = %{tl_version}
Provides:       tex(zbv_igsfta.enc) = %{tl_version}, tex(zbv_ik76ei.enc) = %{tl_version}
Provides:       tex(zbv_ilkd46.enc) = %{tl_version}, tex(zbv_jd6ty7.enc) = %{tl_version}
Provides:       tex(zbv_jmvj36.enc) = %{tl_version}, tex(zbv_jwmruw.enc) = %{tl_version}
Provides:       tex(zbv_k3ascw.enc) = %{tl_version}, tex(zbv_k6hbcl.enc) = %{tl_version}
Provides:       tex(zbv_krjs6b.enc) = %{tl_version}, tex(zbv_l7sulo.enc) = %{tl_version}
Provides:       tex(zbv_lewyuf.enc) = %{tl_version}, tex(zbv_mvsyl4.enc) = %{tl_version}
Provides:       tex(zbv_n3xo7h.enc) = %{tl_version}, tex(zbv_n57xi2.enc) = %{tl_version}
Provides:       tex(zbv_nak3zo.enc) = %{tl_version}, tex(zbv_ne5zxs.enc) = %{tl_version}
Provides:       tex(zbv_nq5ldf.enc) = %{tl_version}, tex(zbv_oue4qy.enc) = %{tl_version}
Provides:       tex(zbv_riybhr.enc) = %{tl_version}, tex(zbv_rtdlfq.enc) = %{tl_version}
Provides:       tex(zbv_rzwiio.enc) = %{tl_version}, tex(zbv_shb4ap.enc) = %{tl_version}
Provides:       tex(zbv_uhxou6.enc) = %{tl_version}, tex(zbv_untte3.enc) = %{tl_version}
Provides:       tex(zbv_upsxpb.enc) = %{tl_version}, tex(zbv_wvrs5w.enc) = %{tl_version}
Provides:       tex(zbv_wy43ep.enc) = %{tl_version}, tex(zbv_xbckbj.enc) = %{tl_version}
Provides:       tex(zbv_xjuza2.enc) = %{tl_version}, tex(zbv_xsxsev.enc) = %{tl_version}
Provides:       tex(zbv_xyk42r.enc) = %{tl_version}, tex(zbv_ymibyh.enc) = %{tl_version}
Provides:       tex(baskervaldx.map) = %{tl_version}, tex(Baskervaldx-Bol.otf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta.otf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita.otf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg.otf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-sup-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-alph.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-sup-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-alph.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-sup-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-sup-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-osf.tfm) = %{tl_version}
Provides:       tex(zbvbmi.tfm) = %{tl_version}, tex(zbvmi.tfm) = %{tl_version}
Provides:       tex(Baskervaldx-Bol.pfb) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta.pfb) = %{tl_version}
Provides:       tex(Baskervaldx-Ita.pfb) = %{tl_version}
Provides:       tex(Baskervaldx-Reg.pfb) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-lf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-osf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-sup-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-sup-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Bol-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-lf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-osf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-sup-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-sup-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-BolIta-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-lf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-osf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-sup-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-sup-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Ita-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-lf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-osf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-sup-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-sup-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-t1.vf) = %{tl_version}
Provides:       tex(Baskervaldx-Reg-tosf-ts1.vf) = %{tl_version}
Provides:       tex(zbvbmi.vf) = %{tl_version}, tex(zbvmi.vf) = %{tl_version}
Provides:       tex(Baskervaldx.sty) = %{tl_version}, tex(LY1Baskervaldx-LF.fd) = %{tl_version}
Provides:       tex(LY1Baskervaldx-OsF.fd) = %{tl_version}
Provides:       tex(LY1Baskervaldx-Sup.fd) = %{tl_version}
Provides:       tex(LY1Baskervaldx-TLF.fd) = %{tl_version}
Provides:       tex(LY1Baskervaldx-TOsF.fd) = %{tl_version}
Provides:       tex(T1Baskervaldx-LF.fd) = %{tl_version}
Provides:       tex(T1Baskervaldx-OsF.fd) = %{tl_version}
Provides:       tex(T1Baskervaldx-Sup.fd) = %{tl_version}
Provides:       tex(T1Baskervaldx-TLF.fd) = %{tl_version}
Provides:       tex(T1Baskervaldx-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Baskervaldx-LF.fd) = %{tl_version}
Provides:       tex(TS1Baskervaldx-OsF.fd) = %{tl_version}
Provides:       tex(TS1Baskervaldx-TLF.fd) = %{tl_version}
Provides:       tex(TS1Baskervaldx-TOsF.fd) = %{tl_version}

%description -n texlive-baskervaldx
Extends and modifies the BaskervaldADF font (a Baskerville
substitute) with more accented glyphs, with small caps and
oldstyle figures in all shapes. Includes OpenType and
PostScript fonts, as well as LaTeX support files.

%package -n texlive-baskervaldx-doc
Summary:        Documentation for baskervaldx
Version:        svn43461
Provides:       tex-baskervaldx-doc
AutoReqProv:    No

%description -n texlive-baskervaldx-doc
Documentation for baskervaldx

%package -n texlive-basque-book
Provides:       tex-basque-book = %{tl_version}
License:        LPPL 1.2
Summary:        Class for book-type documents written in Basque
Version:        svn32924.1.20

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(basque-date.sty)
Provides:       tex(basque-book.cls) = %{tl_version}

%description -n texlive-basque-book
The class is derived from the LaTeX book class. The extensions
solve grammatical and numeration issues that occur when book-
type documents are written in Basque. The class is useful for
writing books, PhD and Master Theses, etc., in Basque.

%package -n texlive-basque-book-doc
Summary:        Documentation for basque-book
Version:        svn32924.1.20

Provides:       tex-basque-book-doc
AutoReqProv:    No

%description -n texlive-basque-book-doc
Documentation for basque-book

%package -n texlive-basque-date
Provides:       tex-basque-date = %{tl_version}
License:        LPPL 1.2
Summary:        Print the date in Basque
Version:        svn26477.1.05

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(basque-date.sty) = %{tl_version}

%description -n texlive-basque-date
The package provides two LaTeX commands to print the current
date in Basque according to the correct forms ruled by The
Basque Language Academy (Euskaltzaindia). The commands
automatically solve the complex declination issues of numbers
in Basque.

%package -n texlive-basque-date-doc
Summary:        Documentation for basque-date
Version:        svn26477.1.05

Provides:       tex-basque-date-doc
AutoReqProv:    No

%description -n texlive-basque-date-doc
Documentation for basque-date

%package -n texlive-bbcard
Provides:       tex-bbcard = %{tl_version}
License:        Public Domain
Summary:        Bullshit bingo, calendar and baseball-score cards
Version:        svn19440.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-bbcard
Three jiffy packages for creating cards of various sorts with
MetaPost.

%package -n texlive-bbcard-doc
Summary:        Documentation for bbcard
Version:        svn19440.0

Provides:       tex-bbcard-doc
AutoReqProv:    No

%description -n texlive-bbcard-doc
Documentation for bbcard

%package -n texlive-asapsym-doc
Provides:       tex-asapsym-doc = %{tl_version}
License:        LPPL
Summary:        doc files of asapsym
Version:        svn40201

AutoReqProv:    No

%description -n texlive-asapsym-doc
Documentation for asapsym

%package -n texlive-asapsym
Provides:       tex-asapsym = %{tl_version}
License:        LPPL
Summary:        Using the free ASAP Symbol font with LaTeX and Plain TeX
Version:        svn40201

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(asapsym.sty) = %{tl_version}, tex(asapsym-generic.tex) = %{tl_version}
Provides:       tex(asapsym.code.tex) = %{tl_version}, tex(Asap-Symbol.otf) = %{tl_version}

%description -n texlive-asapsym
The package provides macros (usable with LaTeX or Plain TeX)
for using the freely available ASAP Symbol font, which is also
included. The font is distributed in OpenType format, and makes
extensive use of OpenType features. Therefore, at this time,
only XeTeX and LuaTeX are supported. An error message is issued
if an OTF-capable engine is not detected.

%package -n texlive-asciilist-doc
Provides:       tex-asciilist-doc = %{tl_version}
License:        LPPL
Summary:        doc files of asciilist
Version:        svn41158
AutoReqProv:    No

%description -n texlive-asciilist-doc
Documentation for asciilist

%package -n texlive-asciilist
Provides:       tex-asciilist = %{tl_version}
License:        LPPL
Summary:        Environments AsciiList and AsciiDocList for prototyping nested lists in LaTeX.
Version:        svn41158
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(asciilist.sty) = %{tl_version}

%description -n texlive-asciilist
The asciilist provides the environments AsciiList and
AsciiDocList, which enable quickly typesetting nested lists in
LaTeX without having to type individual item macros or
opening/closing list environments. The package provides
auxiliary functionality for loading such lists from files and
provides macros for configuring the use of the list
environments and the appearance of the typeset results.

%package -n texlive-babel-belarusian-doc
Provides:       tex-babel-belarusian-doc = %{tl_version}
License:        LPPL
Summary:        doc files of babel-belarusian
Version:        svn40636

AutoReqProv:    No

%description -n texlive-babel-belarusian-doc
Documentation for babel-belarusian

%package -n texlive-babel-belarusian
Provides:       tex-babel-belarusian = %{tl_version}
License:        LPPL
Summary:        Babel support for Belarusian
Version:        svn40636

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(belarusianb.ldf) = %{tl_version}

%description -n texlive-babel-belarusian
The package provides support for use of Babel in documents
written in Belarusian.

%package -n texlive-babel-macedonian-doc
Provides:       tex-babel-macedonian-doc = %{tl_version}
License:        LPPL
Summary:        doc files of babel-macedonian
Version:        svn39587

AutoReqProv:    No

%description -n texlive-babel-macedonian-doc
Documentation for babel-macedonian

%package -n texlive-babel-macedonian
Provides:       tex-babel-macedonian = %{tl_version}
License:        LPPL
Summary:        Babel module to support Macedonian Cyrillic
Version:        svn39587

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(macedonian.ldf) = %{tl_version}

%description -n texlive-babel-macedonian
The package provides support for Macedonian documents written
in Cyrillic, in babel.

%package -n texlive-babel-occitan-doc
Provides:       tex-babel-occitan-doc = %{tl_version}
License:        LPPL
Summary:        doc files of babel-occitan
Version:        svn39608

AutoReqProv:    No

%description -n texlive-babel-occitan-doc
Documentation for babel-occitan

%package -n texlive-babel-occitan
Provides:       tex-babel-occitan = %{tl_version}
License:        LPPL
Summary:        Babel support for Occitan
Version:        svn39608

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(occitan.ldf) = %{tl_version}

%description -n texlive-babel-occitan
Occitan language description file with usage instructions.

%package -n texlive-babel-vietnamese-doc
Provides:       tex-babel-vietnamese-doc = %{tl_version}
License:        LPPL
Summary:        doc files of babel-vietnamese
Version:        svn39246

AutoReqProv:    No

%description -n texlive-babel-vietnamese-doc
Documentation for babel-vietnamese

%package -n texlive-arphic-ttf
Summary:        TrueType version of Chinese Arphic fonts
Version:        svn42675
License:        Arphic
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bkai00mp.ttf) = %{tl_version}, tex(bsmi00lp.ttf) = %{tl_version}
Provides:       tex(gbsn00lp.ttf) = %{tl_version}, tex(gkai00mp.ttf) = %{tl_version}

%description -n texlive-arphic-ttf
This package provides TrueType versions of the Chinese Arphic
fonts for use with XeLaTeX and LuaLaTeX. Type1 versions of
these fonts, for use with pdfLaTeX and the cjk package, are
provided by the arphic package. Arphic is actually the name of
the company which created these fonts.

%package -n texlive-asymptote-by-example-zh-cn-doc
Summary:        doc files of asymptote-by-example-zh-cn
Version:        svn15878
License:        GPLv3+

%description -n texlive-asymptote-by-example-zh-cn-doc
Chinese translation of asymptote by example.

%package -n texlive-asymptote-faq-zh-cn-doc
Summary:        doc files of asymptote-faq-zh-cn
Version:        svn15878
License:        GPLv3+

%description -n texlive-asymptote-faq-zh-cn-doc
Chinese translation of asymptote faq.

%package -n texlive-asymptote-manual-zh-cn-doc
Summary:        doc files of asymptote-manual-zh-cn
Version:        svn15878
License:        GPLv3+

%description -n texlive-asymptote-manual-zh-cn-doc
Chinese translation of asymptote manual.

%package -n texlive-aucklandthesis
Summary:        Memoir-based class for formatting University of Auckland masters' and doctors' theses.
Version:        svn41506
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(aucklandthesis.cls) = %{tl_version}

%description -n texlive-aucklandthesis
A memoir-based class for formatting University of Auckland
masters' and doctors' thesis dissertations in any discipline.
The title page does not handle short dissertations for
diplomas.

%package -n texlive-aurl
Summary:        Extends the hyperref package with a mechanism for hyperlinked URLs abbreviated with prefixes
Version:        svn41853
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(aurl.sty) = %{tl_version}

%description -n texlive-aurl
Semantic Web resource URLs are often abbreviated with prefixes,
like "owl:Class" or "rdf:type". The abbreviated URL (aurl)
package provides the correct hyperlinks for those URLs. The
1000 most common prefixes are predefined and more can be added.

%package -n texlive-awesomebox
Summary:        Draw admonition blocks in your documents, illustrated with FontAwesome icons
Version:        svn46513
License:        WTFPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(awesomebox.sty) = %{tl_version}

%description -n texlive-awesomebox
Awesome Boxes is all about drawing admonition blocks around
text to inform or alert readers about something particular. The
specific aim of this package is to use FontAwesome icons to
ease the illustration of these blocks. This package requires
FontAwesome and XeLaTeX or LuaLaTeX.

%package -n texlive-babel-azerbaijani
Summary:        Support for Azerbaijani within babel
Version:        svn44197
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%description -n texlive-babel-azerbaijani
This is the babel style for Azerbaijani. This language poses
special challenges because no "traditional" font encoding
contains the full character set, and therefore a mixture must
be used (e.g., T2A and T1). This package is compatible with
Unicode engines (LuaTeX, XeTeX), which are very likely the most
convenient way to write Azerbaijani documents.

%package -n texlive-baekmuk
Summary:        Baekmuk Korean TrueType fonts
Version:        svn42106
License:        Baekmuk
Requires:       texlive-base texlive-kpathsea
Provides:       tex(batang.ttf) = %{tl_version}, tex(dotum.ttf) = %{tl_version}
Provides:       tex(gulim.ttf) = %{tl_version}, tex(hline.ttf) = %{tl_version}

%description -n texlive-baekmuk
Baekmuk TrueType fonts (Korean) These fonts were retrieved from
http://kldp.net/baekmuk/

%package -n texlive-bangorexam
Summary:        Typeset an examination at Bangor University
Version:        svn46626
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bangorexam.cls) = %{tl_version}

%description -n texlive-bangorexam
The package allows typesetting of Bangor Univesity's exam
style. It currently supports a standard A/B choice, A-only
compulsory and 'n' from 'm' exam styles. Marks are totalled and
checked automatically.

%package -n texlive-baskervillef
Summary:        Fry's Baskerville look-alike, with math support
Version:        svn45651
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(zba_3oppw2.enc) = %{tl_version}, tex(zba_4scfns.enc) = %{tl_version}
Provides:       tex(zba_523v7l.enc) = %{tl_version}, tex(zba_66iezk.enc) = %{tl_version}
Provides:       tex(zba_6emqgt.enc) = %{tl_version}, tex(zba_6mhi2z.enc) = %{tl_version}
Provides:       tex(zba_77ryg7.enc) = %{tl_version}, tex(zba_7yyqda.enc) = %{tl_version}
Provides:       tex(zba_a6zfty.enc) = %{tl_version}, tex(zba_adnnkl.enc) = %{tl_version}
Provides:       tex(zba_ahcsm7.enc) = %{tl_version}, tex(zba_b5lrlg.enc) = %{tl_version}
Provides:       tex(zba_bnmcfu.enc) = %{tl_version}, tex(zba_bue3wb.enc) = %{tl_version}
Provides:       tex(zba_bvbtx2.enc) = %{tl_version}, tex(zba_cgvvj5.enc) = %{tl_version}
Provides:       tex(zba_csuamn.enc) = %{tl_version}, tex(zba_cvjygd.enc) = %{tl_version}
Provides:       tex(zba_cyyuxb.enc) = %{tl_version}, tex(zba_dzrx7a.enc) = %{tl_version}
Provides:       tex(zba_e3xw3x.enc) = %{tl_version}, tex(zba_e6c7a3.enc) = %{tl_version}
Provides:       tex(zba_eurn55.enc) = %{tl_version}, tex(zba_evqzha.enc) = %{tl_version}
Provides:       tex(zba_fj77ru.enc) = %{tl_version}, tex(zba_hkkd2g.enc) = %{tl_version}
Provides:       tex(zba_hljrbf.enc) = %{tl_version}, tex(zba_i3q27v.enc) = %{tl_version}
Provides:       tex(zba_i5fury.enc) = %{tl_version}, tex(zba_igqvi4.enc) = %{tl_version}
Provides:       tex(zba_invrxa.enc) = %{tl_version}, tex(zba_iqxfxn.enc) = %{tl_version}
Provides:       tex(zba_iy3fha.enc) = %{tl_version}, tex(zba_iy3qnl.enc) = %{tl_version}
Provides:       tex(zba_jayro7.enc) = %{tl_version}, tex(zba_jesydd.enc) = %{tl_version}
Provides:       tex(zba_kb3ura.enc) = %{tl_version}, tex(zba_kodzea.enc) = %{tl_version}
Provides:       tex(zba_koujiy.enc) = %{tl_version}, tex(zba_kqfmr4.enc) = %{tl_version}
Provides:       tex(zba_kragcu.enc) = %{tl_version}, tex(zba_kua26b.enc) = %{tl_version}
Provides:       tex(zba_kuzvvg.enc) = %{tl_version}, tex(zba_ljx3jq.enc) = %{tl_version}
Provides:       tex(zba_lwrbox.enc) = %{tl_version}, tex(zba_m3z5kj.enc) = %{tl_version}
Provides:       tex(zba_mebvzg.enc) = %{tl_version}, tex(zba_mevjdz.enc) = %{tl_version}
Provides:       tex(zba_n43ddx.enc) = %{tl_version}, tex(zba_n4mxmz.enc) = %{tl_version}
Provides:       tex(zba_nvjtae.enc) = %{tl_version}, tex(zba_o2tifi.enc) = %{tl_version}
Provides:       tex(zba_o6dtj2.enc) = %{tl_version}, tex(zba_owa6ha.enc) = %{tl_version}
Provides:       tex(zba_owjda7.enc) = %{tl_version}, tex(zba_oxcsv2.enc) = %{tl_version}
Provides:       tex(zba_oyegn6.enc) = %{tl_version}, tex(zba_p3pzma.enc) = %{tl_version}
Provides:       tex(zba_pjh6nq.enc) = %{tl_version}, tex(zba_pqfamk.enc) = %{tl_version}
Provides:       tex(zba_q37ime.enc) = %{tl_version}, tex(zba_qleltn.enc) = %{tl_version}
Provides:       tex(zba_qptswd.enc) = %{tl_version}, tex(zba_qycpdj.enc) = %{tl_version}
Provides:       tex(zba_rqwz3b.enc) = %{tl_version}, tex(zba_s6fzkp.enc) = %{tl_version}
Provides:       tex(zba_sb5wfb.enc) = %{tl_version}, tex(zba_sqc4ly.enc) = %{tl_version}
Provides:       tex(zba_t5goht.enc) = %{tl_version}, tex(zba_t7zhq6.enc) = %{tl_version}
Provides:       tex(zba_taxp3x.enc) = %{tl_version}, tex(zba_tjuaha.enc) = %{tl_version}
Provides:       tex(zba_tqvuvp.enc) = %{tl_version}, tex(zba_twn2qn.enc) = %{tl_version}
Provides:       tex(zba_u24co6.enc) = %{tl_version}, tex(zba_uf7ozb.enc) = %{tl_version}
Provides:       tex(zba_vaofbk.enc) = %{tl_version}, tex(zba_ve4agh.enc) = %{tl_version}
Provides:       tex(zba_vezlo5.enc) = %{tl_version}, tex(zba_vunabj.enc) = %{tl_version}
Provides:       tex(zba_wcz3px.enc) = %{tl_version}, tex(zba_wdfmp4.enc) = %{tl_version}
Provides:       tex(zba_xlbenp.enc) = %{tl_version}, tex(zba_xt7x67.enc) = %{tl_version}
Provides:       tex(zba_xucdkt.enc) = %{tl_version}, tex(zba_z5rfyo.enc) = %{tl_version}
Provides:       tex(zba_zfeutd.enc) = %{tl_version}, tex(zba_zn4iv3.enc) = %{tl_version}
Provides:       tex(zba_zptsj3.enc) = %{tl_version}, tex(zba_zygn7r.enc) = %{tl_version}
Provides:       tex(BaskervilleF.map) = %{tl_version}, tex(BaskervilleF-Bold.otf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic.otf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic.otf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular.otf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-alph.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-alph.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Italic.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Regular.tfm) = %{tl_version}
Provides:       tex(zbabmi.tfm) = %{tl_version}, tex(zbami.tfm) = %{tl_version}
Provides:       tex(BaskervilleF-Bold.pfb) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic.pfb) = %{tl_version}
Provides:       tex(BaskervilleF-Italic.pfb) = %{tl_version}
Provides:       tex(BaskervilleF-Regular.pfb) = %{tl_version}
Provides:       tex(baskervillef.sty) = %{tl_version}, tex(BaskervilleF-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-dnom-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-th-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-th-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-th-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-th-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(BaskervilleF-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(zbabmi.vf) = %{tl_version}, tex(zbami.vf) = %{tl_version}
Provides:       tex(LY1BaskervilleF-Dnom.fd) = %{tl_version}
Provides:       tex(LY1BaskervilleF-LF.fd) = %{tl_version}
Provides:       tex(LY1BaskervilleF-OsF.fd) = %{tl_version}
Provides:       tex(LY1BaskervilleF-Sup.fd) = %{tl_version}
Provides:       tex(LY1BaskervilleF-TLF.fd) = %{tl_version}
Provides:       tex(LY1BaskervilleF-TOsF.fd) = %{tl_version}
Provides:       tex(OT1BaskervilleF-Dnom.fd) = %{tl_version}
Provides:       tex(OT1BaskervilleF-LF.fd) = %{tl_version}
Provides:       tex(OT1BaskervilleF-OsF.fd) = %{tl_version}
Provides:       tex(OT1BaskervilleF-Sup.fd) = %{tl_version}
Provides:       tex(OT1BaskervilleF-TLF.fd) = %{tl_version}
Provides:       tex(OT1BaskervilleF-TOsF.fd) = %{tl_version}
Provides:       tex(T1BaskervilleF-Dnom.fd) = %{tl_version}
Provides:       tex(T1BaskervilleF-LF.fd) = %{tl_version}
Provides:       tex(T1BaskervilleF-OsF.fd) = %{tl_version}
Provides:       tex(T1BaskervilleF-Sup.fd) = %{tl_version}
Provides:       tex(T1BaskervilleF-TLF.fd) = %{tl_version}
Provides:       tex(T1BaskervilleF-TOsF.fd) = %{tl_version}
Provides:       tex(TS1BaskervilleF-LF.fd) = %{tl_version}
Provides:       tex(TS1BaskervilleF-OsF.fd) = %{tl_version}
Provides:       tex(TS1BaskervilleF-TLF.fd) = %{tl_version}
Provides:       tex(TS1BaskervilleF-TOsF.fd) = %{tl_version}
Provides:       tex(omlzbami.fd) = %{tl_version}

%description -n texlive-baskervillef
BaskervilleF is a fork from the Libre Baskerville fonts (Roman,
Italic, Bold only) released under the OFL by Paolo Impallari
and Rodrigo Fuenzalida. Their fonts are optimized for web
usage, while BaskervilleF is optimized for traditional TeX
usage, normally destined for production of pdf files. A bold
italic style was added and mathematical support is offered as
an option to newtxmath.

%package -n texlive-autoaligne
Summary:        Align terms and members in math expressions
Version:        svn43195
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(autoaligne-fr.tex) = %{tl_version}, tex(autoaligne.sty) = %{tl_version}
Provides:       tex(autoaligne.tex) = %{tl_version}

%description -n texlive-autoaligne
This package allows to align terms and members between lines
containing math expressions.

%package -n texlive-ascmac
Summary:        Boxes and picture macros with Japanese vertical writing support
Version:        svn46904
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ascmac.sty) = %{tl_version}, tex(tascmac.sty) = %{tl_version}
Provides:       tex(ascgrp.mf) = %{tl_version}, tex(ascii.mf) = %{tl_version}
Provides:       tex(ascii10.mf) = %{tl_version}, tex(ascii36.mf) = %{tl_version}
Provides:       tex(ascgrp.tfm) = %{tl_version}, tex(ascii10.tfm) = %{tl_version}
Provides:       tex(ascii36.tfm) = %{tl_version}, tex(ascgrp.pfb) = %{tl_version}
Provides:       tex(ascii10.pfb) = %{tl_version}, tex(ascii36.pfb) = %{tl_version}

%description -n texlive-ascmac
The bundle provides boxes and picture macros with Japanese
vertical writing support. It uses only native picture macros
and fonts for drawing boxes and is thus driver-independent.
Formerly part of the Japanese pLaTeX bundle, it now supports
all LaTeX engines.

%package -n texlive-authorarchive
Summary:        Adds self-archiving information to scientific papers
Version:        svn46704
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(authorarchive.sty) = %{tl_version}

%description -n texlive-authorarchive
This is a LaTeX style for producing author self-archiving
copies of (academic) papers. The following layout-styles are
pre-defined: ACMfor the two-column layout used by many ACM
conferences IEEE for the two-column layout used by many IEEE
conferences LNCS for the LNCS layout (as used by Springer) LNI
for the Lecture Notes in Informatics, published by the GI ENTCS
for the Elsevier ENTCS layout

%package -n texlive-autobreak
Summary:        Simple line breaking of long formulae
Version:        svn43337
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(autobreak.sty) = %{tl_version}

%description -n texlive-autobreak
This package implements a simple mechanism of line/page
breaking within the align environment of the amsmath package;
new line characters are considered as possible candidates for
the breaks and the package tries to put breaks at adequate
places. It is suitable for computer-generated long formulae
with many terms.

%package -n texlive-auto-pst-pdf-lua
Summary:        Using LuaLaTeX together with PostScript code
Version:        svn47028
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(ifpdf.sty)
Requires:       tex(ifluatex.sty), tex(ifplatform.sty), tex(xkeyval.sty)
Provides:       tex(auto-pst-pdf-lua.sty) = %{tl_version}

%description -n texlive-auto-pst-pdf-lua
This package is a slightly modified version of auto-pst-pdf by
Will Robertson, which itself is a wrapper for pst-pdf by Rolf
Niepraschk. The package allows the use of LuaLaTeX together
with PostScript related code, eg. PSTricks. It depends on
ifpdf, ifluatex, ifplatform, and xkeyval.

%package -n texlive-babel-japanese
Summary:        Babel support for Japanes
Version:        svn43145
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(japanese.ldf) = %{tl_version}

%description -n texlive-babel-japanese
This package provides a japanese option for the babel package.
It defines all the language definition macros in Japanese.
Currently this package works with pLaTeX, upLaTeX, XeLaTeX and
LuaLaTeX.

%package -n texlive-bath-bst
Summary:        Harvard referencing style as recommended by the University of Bath Library
Version:        svn47507
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bath.bst) = %{tl_version}, tex(bathx.bst) = %{tl_version}

%description -n texlive-bath-bst
This package provides a BibTeX style to format reference lists
in the Harvard style recommended by the University of Bath
Library. It should be used in conjunction with natbib for
citations.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/baskervaldx"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-around-the-bend-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/around-the-bend/

%files -n texlive-arrayjobx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/arrayjobx/

%files -n texlive-arrayjobx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/arrayjobx/

%files -n texlive-arraysort
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/arraysort/

%files -n texlive-arraysort-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/arraysort/

%files -n texlive-arphic
%license other-free.txt
%{_texdir}/texmf-dist/dvips/arphic/
%{_texdir}/texmf-dist/fonts/afm/arphic/
%{_texdir}/texmf-dist/fonts/map/dvips/arphic/
%{_texdir}/texmf-dist/fonts/tfm/arphic/
%{_texdir}/texmf-dist/fonts/type1/arphic/
%{_texdir}/texmf-dist/fonts/vf/arphic/

%files -n texlive-arphic-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/fonts/arphic/

%files -n texlive-arsclassica
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/arsclassica/

%files -n texlive-arsclassica-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/arsclassica/

%files -n texlive-articleingud
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/articleingud/

%files -n texlive-articleingud-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/articleingud/

%files -n texlive-arydshln
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/arydshln/

%files -n texlive-arydshln-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/arydshln/

%files -n texlive-asaetr
%license pd.txt
%{_texdir}/texmf-dist/bibtex/bst/asaetr/
%{_texdir}/texmf-dist/tex/latex/asaetr/

%files -n texlive-asaetr-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/asaetr/


%files -n texlive-ascelike
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/ascelike/
%{_texdir}/texmf-dist/tex/latex/ascelike/

%files -n texlive-ascelike-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ascelike/

%files -n texlive-ascii-chart-doc
%{_texdir}/texmf-dist/doc/support/ascii-chart/

%files -n texlive-ascii-font
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/ascii-font/
%{_texdir}/texmf-dist/fonts/tfm/public/ascii-font/
%{_texdir}/texmf-dist/fonts/type1/public/ascii-font/
%{_texdir}/texmf-dist/tex/latex/ascii-font/

%files -n texlive-ascii-font-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/ascii-font/

%files -n texlive-askmaps
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/askmaps/

%files -n texlive-askmaps-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/askmaps/

%files -n texlive-aspectratio
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/aspectratio/
%{_texdir}/texmf-dist/fonts/source/public/aspectratio/
%{_texdir}/texmf-dist/fonts/tfm/public/aspectratio/
%{_texdir}/texmf-dist/fonts/type1/public/aspectratio/
%{_texdir}/texmf-dist/tex/latex/aspectratio/

%files -n texlive-aspectratio-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/aspectratio/

%files -n texlive-assignment
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/assignment/

%files -n texlive-assignment-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/assignment/

%files -n texlive-assoccnt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/assoccnt/

%files -n texlive-assoccnt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/assoccnt/

%files -n texlive-astro
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/astro/
%{_texdir}/texmf-dist/fonts/tfm/public/astro/

%files -n texlive-astro-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/astro/

%files -n texlive-asyfig
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/asyfig/

%files -n texlive-asyfig-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/asyfig/

%files -n texlive-asypictureb
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/asypictureb/

%files -n texlive-asypictureb-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/asypictureb/

%files -n texlive-attachfile
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/attachfile/
%{_texdir}/texmf-dist/bibtex/bib/attachfile/

%files -n texlive-attachfile-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/attachfile/

%files -n texlive-augie
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/augie/
%{_texdir}/texmf-dist/fonts/map/dvips/augie/
%{_texdir}/texmf-dist/fonts/tfm/public/augie/
%{_texdir}/texmf-dist/fonts/type1/public/augie/
%{_texdir}/texmf-dist/fonts/vf/public/augie/
%{_texdir}/texmf-dist/tex/latex/augie/

%files -n texlive-augie-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/augie/

%files -n texlive-auncial-new
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/auncial-new/
%{_texdir}/texmf-dist/fonts/map/dvips/auncial-new/
%{_texdir}/texmf-dist/fonts/tfm/public/auncial-new/
%{_texdir}/texmf-dist/fonts/type1/public/auncial-new/
%{_texdir}/texmf-dist/tex/latex/auncial-new/

%files -n texlive-auncial-new-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/auncial-new/

%files -n texlive-aurical
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/aurical/
%{_texdir}/texmf-dist/fonts/map/dvips/aurical/
%{_texdir}/texmf-dist/fonts/source/public/aurical/
%{_texdir}/texmf-dist/fonts/tfm/public/aurical/
%{_texdir}/texmf-dist/fonts/type1/public/aurical/
%{_texdir}/texmf-dist/tex/latex/aurical/

%files -n texlive-aurical-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/aurical/

%files -n texlive-authoraftertitle
%{_texdir}/texmf-dist/tex/latex/authoraftertitle/

%files -n texlive-authoraftertitle-doc
%{_texdir}/texmf-dist/doc/latex/authoraftertitle/

%files -n texlive-autoarea
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/autoarea/

%files -n texlive-autoarea-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/autoarea/

%files -n texlive-automata
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/automata/

%files -n texlive-automata-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/automata/

%files -n texlive-autonum
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/autonum/

%files -n texlive-autonum-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/autonum/

%files -n texlive-autopdf
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/autopdf/

%files -n texlive-autopdf-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/autopdf/

%files -n texlive-auto-pst-pdf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/auto-pst-pdf/

%files -n texlive-auto-pst-pdf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/auto-pst-pdf/

%files -n texlive-avantgar
%license gpl.txt
%{_texdir}/texmf-dist/dvips/avantgar/
%{_texdir}/texmf-dist/fonts/afm/adobe/avantgar/
%{_texdir}/texmf-dist/fonts/afm/urw/avantgar/
%{_texdir}/texmf-dist/fonts/map/dvips/avantgar/
%{_texdir}/texmf-dist/fonts/tfm/adobe/avantgar/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/avantgar/
%{_texdir}/texmf-dist/fonts/type1/urw/avantgar/
%{_texdir}/texmf-dist/fonts/vf/adobe/avantgar/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/avantgar/
%{_texdir}/texmf-dist/tex/latex/avantgar/

%files -n texlive-avremu
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/avremu/

%files -n texlive-avremu-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/avremu/

%files -n texlive-b1encoding
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/b1encoding/
%{_texdir}/texmf-dist/tex/latex/b1encoding/

%files -n texlive-b1encoding-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/b1encoding/

%files -n texlive-babel-albanian
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/babel-albanian/

%files -n texlive-babel-albanian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/babel-albanian/

%files -n texlive-babel-bahasa

%files -n texlive-babel-bahasa-doc

%files -n texlive-babel-indonesian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-indonesian/

%files -n texlive-babel-indonesian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-indonesian/

%files -n texlive-babel-malay
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-malay/

%files -n texlive-babel-malay-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-malay/

%files -n texlive-babel-basque
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-basque/

%files -n texlive-babel-basque-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-basque/

%files -n texlive-babelbib
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/babelbib/
%{_texdir}/texmf-dist/tex/latex/babelbib/

%files -n texlive-babelbib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/babelbib/

%files -n texlive-babel-bosnian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-bosnian/

%files -n texlive-babel-bosnian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-bosnian/

%files -n texlive-babel-breton
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-breton/

%files -n texlive-babel-breton-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-breton/

%files -n texlive-babel-bulgarian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-bulgarian/

%files -n texlive-babel-bulgarian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-bulgarian/

%files -n texlive-babel-catalan
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-catalan/

%files -n texlive-babel-catalan-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-catalan/

%files -n texlive-babel-croatian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-croatian/

%files -n texlive-babel-croatian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-croatian/

%files -n texlive-babel-czech
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-czech/

%files -n texlive-babel-czech-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-czech/

%files -n texlive-babel-danish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-danish/

%files -n texlive-babel-danish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-danish/

%files -n texlive-babel-dutch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-dutch/

%files -n texlive-babel-dutch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-dutch/

%files -n texlive-babel-english
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-english/

%files -n texlive-babel-english-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-english/

%files -n texlive-babel-esperanto
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-esperanto/

%files -n texlive-babel-esperanto-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-esperanto/

%files -n texlive-babel-estonian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-estonian/

%files -n texlive-babel-estonian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-estonian/

%files -n texlive-babel-finnish
%{_texdir}/texmf-dist/tex/generic/babel-finnish/

%files -n texlive-babel-finnish-doc
%{_texdir}/texmf-dist/doc/generic/babel-finnish/

%files -n texlive-babel-french
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-french/

%files -n texlive-babel-french-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-french/

%files -n texlive-babel-friulan
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-friulan/

%files -n texlive-babel-friulan-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-friulan/

%files -n texlive-babel-galician
%{_texdir}/texmf-dist/tex/generic/babel-galician/

%files -n texlive-babel-galician-doc
%{_texdir}/texmf-dist/doc/generic/babel-galician/

%files -n texlive-babel-georgian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-georgian/

%files -n texlive-babel-georgian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-georgian/

%files -n texlive-babel-german
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-german/

%files -n texlive-babel-german-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-german/

%files -n texlive-babel-greek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-greek/

%files -n texlive-babel-greek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-greek/

%files -n texlive-babel-hebrew
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-hebrew/

%files -n texlive-babel-hebrew-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-hebrew/

%files -n texlive-babel-hungarian
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/babel-hungarian/

%files -n texlive-babel-hungarian-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/babel-hungarian/

%files -n texlive-babel-icelandic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-icelandic/

%files -n texlive-babel-icelandic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-icelandic/

%files -n texlive-babel-interlingua
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-interlingua/

%files -n texlive-babel-interlingua-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-interlingua/

%files -n texlive-babel-irish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-irish/

%files -n texlive-babel-irish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-irish/

%files -n texlive-babel-italian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-italian/

%files -n texlive-babel-italian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-italian/

%files -n texlive-babel-kurmanji
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-kurmanji/

%files -n texlive-babel-kurmanji-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-kurmanji/

%files -n texlive-babel-latin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/babel-latin/

%files -n texlive-babel-latin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/babel-latin/

%files -n texlive-babel-latvian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-latvian/

%files -n texlive-babel-latvian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-latvian/

%files -n texlive-babel-norsk
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-norsk/

%files -n texlive-babel-norsk-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-norsk/

%files -n texlive-babel-piedmontese
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-piedmontese/

%files -n texlive-babel-piedmontese-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-piedmontese/

%files -n texlive-babel-polish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-polish/

%files -n texlive-babel-polish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-polish/

%files -n texlive-babel-portuges
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-portuges/

%files -n texlive-babel-portuges-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-portuges/

%files -n texlive-babel-romanian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-romanian/

%files -n texlive-babel-romanian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-romanian/

%files -n texlive-babel-romansh
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-romansh/

%files -n texlive-babel-romansh-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-romansh/

%files -n texlive-babel-russian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-russian/

%files -n texlive-babel-russian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-russian/

%files -n texlive-babel-samin
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-samin/

%files -n texlive-babel-samin-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-samin/

%files -n texlive-babel-scottish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-scottish/

%files -n texlive-babel-scottish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-scottish/

%files -n texlive-babel-serbianc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-serbianc/

%files -n texlive-babel-serbianc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-serbianc/

%files -n texlive-babel-serbian
%{_texdir}/texmf-dist/tex/generic/babel-serbian/

%files -n texlive-babel-serbian-doc
%{_texdir}/texmf-dist/doc/generic/babel-serbian/

%files -n texlive-babel-slovak
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-slovak/

%files -n texlive-babel-slovak-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-slovak/

%files -n texlive-babel-slovenian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-slovenian/

%files -n texlive-babel-slovenian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-slovenian/

%files -n texlive-babel-sorbian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-sorbian/

%files -n texlive-babel-sorbian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-sorbian/

%files -n texlive-babel-spanglish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-spanglish/

%files -n texlive-babel-spanglish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-spanglish/

%files -n texlive-babel-spanish
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/babel-spanish/

%files -n texlive-babel-spanish-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/babel-spanish/

%files -n texlive-babel-swedish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-swedish/

%files -n texlive-babel-swedish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-swedish/

%files -n texlive-babel-thai
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-thai/

%files -n texlive-babel-thai-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-thai/

%files -n texlive-babel
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/babel/
%{_texdir}/texmf-dist/tex/generic/babel/

%files -n texlive-babel-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/babel/

%files -n texlive-babel-turkish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-turkish/

%files -n texlive-babel-turkish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-turkish/

%files -n texlive-babel-ukrainian
%{_texdir}/texmf-dist/tex/generic/babel-ukrainian/

%files -n texlive-babel-ukrainian-doc
%{_texdir}/texmf-dist/doc/generic/babel-ukrainian/

%files -n texlive-babel-vietnamese
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-vietnamese/

%files -n texlive-babel-welsh
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-welsh/

%files -n texlive-babel-welsh-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-welsh/

%files -n texlive-background
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/background/

%files -n texlive-background-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/background/

%files -n texlive-backnaur
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/backnaur/

%files -n texlive-backnaur-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/backnaur/

%files -n texlive-bagpipe
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/bagpipe/

%files -n texlive-bagpipe-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/bagpipe/

%files -n texlive-bangorcsthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bangorcsthesis/

%files -n texlive-bangorcsthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bangorcsthesis/

%files -n texlive-bangtex
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/bangtex/
%{_texdir}/texmf-dist/fonts/tfm/public/bangtex/
%{_texdir}/texmf-dist/tex/latex/bangtex/

%files -n texlive-bangtex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bangtex/

%files -n texlive-bankstatement
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bankstatement/

%files -n texlive-bankstatement-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bankstatement/

%files -n texlive-barcodes
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/barcodes/
%{_texdir}/texmf-dist/fonts/tfm/public/barcodes/
%{_texdir}/texmf-dist/tex/latex/barcodes/

%files -n texlive-barcodes-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/barcodes/

%files -n texlive-bardiag
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bardiag/

%files -n texlive-bardiag-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bardiag/

%files -n texlive-barr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/barr/

%files -n texlive-barr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/barr/

%files -n texlive-bartel-chess-fonts
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/bartel-chess-fonts/
%{_texdir}/texmf-dist/fonts/tfm/public/bartel-chess-fonts/

%files -n texlive-bartel-chess-fonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/bartel-chess-fonts/

%files -n texlive-bashful
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bashful/

%files -n texlive-bashful-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bashful/

%files -n texlive-basicarith
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/basicarith/

%files -n texlive-basicarith-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/basicarith/

%files -n texlive-baskervald
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/arkandis/baskervald/
%{_texdir}/texmf-dist/fonts/enc/dvips/baskervald/
%{_texdir}/texmf-dist/fonts/map/dvips/baskervald/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/baskervald/
%{_texdir}/texmf-dist/fonts/type1/arkandis/baskervald/
%{_texdir}/texmf-dist/fonts/vf/arkandis/baskervald/
%{_texdir}/texmf-dist/tex/latex/baskervald/

%files -n texlive-baskervald-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/baskervald/

%files -n texlive-baskervaldx
%license gpl.txt
%{_datadir}/fonts/baskervaldx
%{_texdir}/texmf-dist/fonts/afm/public/baskervaldx/
%{_texdir}/texmf-dist/fonts/enc/dvips/baskervaldx/
%{_texdir}/texmf-dist/fonts/map/dvips/baskervaldx/
%{_texdir}/texmf-dist/fonts/opentype/public/baskervaldx/
%{_texdir}/texmf-dist/fonts/tfm/public/baskervaldx/
%{_texdir}/texmf-dist/fonts/type1/public/baskervaldx/
%{_texdir}/texmf-dist/fonts/vf/public/baskervaldx/
%{_texdir}/texmf-dist/tex/latex/baskervaldx/

%files -n texlive-baskervaldx-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/baskervaldx/

%files -n texlive-basque-book
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/basque-book/

%files -n texlive-basque-book-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/basque-book/

%files -n texlive-basque-date
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/basque-date/

%files -n texlive-basque-date-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/basque-date/

%files -n texlive-bbcard
%license pd.txt
%{_texdir}/texmf-dist/metapost/bbcard/

%files -n texlive-bbcard-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/bbcard/


%files -n texlive-asapsym-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/asapsym/

%files -n texlive-asapsym
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/asapsym/
%{_texdir}/texmf-dist/tex/latex/asapsym/
%{_texdir}/texmf-dist/tex/plain/asapsym/
%{_texdir}/texmf-dist/fonts/opentype/omnibus-type/asapsym/

%files -n texlive-asciilist-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/asciilist/

%files -n texlive-asciilist
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/asciilist/

%files -n texlive-babel-belarusian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-belarusian/

%files -n texlive-babel-belarusian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-belarusian/

%files -n texlive-babel-macedonian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-macedonian/

%files -n texlive-babel-macedonian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-macedonian/

%files -n texlive-babel-occitan-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-occitan/

%files -n texlive-babel-occitan
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/babel-occitan/

%files -n texlive-babel-vietnamese-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/babel-vietnamese/

%files -n texlive-arphic-ttf
%doc %{_texdir}/texmf-dist/doc/fonts/arphic-ttf/
%{_texdir}/texmf-dist/fonts/truetype/public/arphic-ttf/

%files -n texlive-asymptote-by-example-zh-cn-doc
%doc %{_texdir}/texmf-dist/doc/support/asymptote-by-example-zh-cn/

%files -n texlive-asymptote-faq-zh-cn-doc
%doc %{_texdir}/texmf-dist/doc/support/asymptote-faq-zh-cn/

%files -n texlive-asymptote-manual-zh-cn-doc
%doc %{_texdir}/texmf-dist/doc/support/asymptote-manual-zh-cn/

%files -n texlive-aucklandthesis
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/aucklandthesis/
%{_texdir}/texmf-dist/tex/latex/aucklandthesis/

%files -n texlive-aurl
%license pd.txt
%doc %{_texdir}/texmf-dist/doc/latex/aurl/
%{_texdir}/texmf-dist/tex/latex/aurl/

%files -n texlive-awesomebox
%doc %{_texdir}/texmf-dist/doc/latex/awesomebox/
%{_texdir}/texmf-dist/tex/latex/awesomebox/

%files -n texlive-babel-azerbaijani
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/babel-azerbaijani/
%{_texdir}/texmf-dist/tex/generic/babel-azerbaijani/

%files -n texlive-baekmuk
%doc %{_texdir}/texmf-dist/doc/fonts/baekmuk/
%{_texdir}/texmf-dist/fonts/truetype/public/baekmuk/

%files -n texlive-bangorexam
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/bangorexam/
%{_texdir}/texmf-dist/tex/latex/bangorexam/

%files -n texlive-baskervillef
%license ofl.txt lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/baskervillef/
%{_texdir}/texmf-dist/fonts/enc/dvips/baskervillef/
%{_texdir}/texmf-dist/fonts/map/dvips/baskervillef/
%{_texdir}/texmf-dist/fonts/opentype/public/baskervillef/
%{_texdir}/texmf-dist/fonts/tfm/public/baskervillef/
%{_texdir}/texmf-dist/fonts/type1/public/baskervillef/
%{_texdir}/texmf-dist/fonts/vf/public/baskervillef/
%{_texdir}/texmf-dist/tex/latex/baskervillef/

%files -n texlive-autoaligne
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/autoaligne/
%{_texdir}/texmf-dist/tex/generic/autoaligne/

%files -n texlive-ascmac
%license bsd.txt
%{_texdir}/texmf-dist/fonts/source/public/ascmac/
%{_texdir}/texmf-dist/fonts/tfm/public/ascmac/
%{_texdir}/texmf-dist/fonts/type1/public/ascmac/
%{_texdir}/texmf-dist/tex/latex/ascmac/
%doc %{_texdir}/texmf-dist/doc/latex/ascmac/

%files -n texlive-authorarchive
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/authorarchive/
%doc %{_texdir}/texmf-dist/doc/latex/authorarchive/

%files -n texlive-autobreak
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/autobreak/
%doc %{_texdir}/texmf-dist/doc/latex/autobreak/

%files -n texlive-auto-pst-pdf-lua
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/auto-pst-pdf-lua/
%doc %{_texdir}/texmf-dist/doc/latex/auto-pst-pdf-lua/

%files -n texlive-babel-japanese
%license lppl.txt
%{_texdir}/texmf-dist/tex/generic/babel-japanese/
%doc %{_texdir}/texmf-dist/doc/generic/babel-japanese/

%files -n texlive-bath-bst
%license lppl.txt
%{_texdir}/texmf-dist/bibtex/bst/bath-bst/
%doc %{_texdir}/texmf-dist/doc/bibtex/bath-bst/



%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
