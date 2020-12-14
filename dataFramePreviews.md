```
>>> df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Badges.parquet")
>>> df.show()                                                                   
+------+--------------------+-------+----------------+---------+-------+        
|_Class|               _Date|    _Id|           _Name|_TagBased|_UserId|
+------+--------------------+-------+----------------+---------+-------+
|     2|2011-02-02T17:42:...|1400008|Notable Question|    false|   3488|
|     2|2011-02-02T17:42:...|1400009|            Guru|    false| 353410|
|     3|2011-02-02T17:47:...|1400010|         Student|    false| 599272|
|     3|2011-02-02T17:47:...|1400011|         Student|    false| 557399|
|     3|2011-02-02T17:47:...|1400012|         Student|    false| 600168|
|     3|2011-02-02T17:47:...|1400013|          Editor|    false| 564626|
|     3|2011-02-02T17:47:...|1400014|  Autobiographer|    false| 296093|
|     3|2011-02-02T17:47:...|1400016|         Scholar|    false| 410592|
|     3|2011-02-02T17:47:...|1400017|         Scholar|    false| 463428|
|     3|2011-02-02T17:47:...|1400018|   Nice Question|    false|  32484|
|     3|2011-02-02T17:47:...|1400019|Popular Question|    false|   1512|
|     3|2011-02-02T17:47:...|1400020|Popular Question|    false|   7453|
|     3|2011-02-02T17:47:...|1400021|Popular Question|    false| 256239|
|     3|2011-02-02T17:47:...|1400022|Popular Question|    false| 326284|
|     3|2011-02-02T17:47:...|1400023|Popular Question|    false|  22215|
|     3|2011-02-02T17:47:...|1400024|      Tumbleweed|    false| 591013|
|     3|2011-02-02T17:47:...|1400025|      Tumbleweed|    false| 591011|
|     3|2011-02-02T17:52:...|1400026|         Student|    false| 543649|
|     3|2011-02-02T17:52:...|1400027|         Student|    false| 553638|
|     3|2011-02-02T17:52:...|1400028|         Student|    false| 155689|
+------+--------------------+-------+----------------+---------+-------+
```


```
>>> spark.read.parquet("/user/***REMOVED***/StackOverflow/Comments.parquet").show()
+---------------+--------------------+-------+-------+------+--------------------+----------------+-------+
|_ContentLicense|       _CreationDate|    _Id|_PostId|_Score|               _Text|_UserDisplayName|_UserId|
+---------------+--------------------+-------+-------+------+--------------------+----------------+-------+
|   CC BY-SA 2.5|2010-07-02T21:17:...|3260274|3168284|     0|So, for each pati...|            null|  32632|
|   CC BY-SA 2.5|2010-07-02T21:17:...|3260275|3167981|     0|Another alternati...|            null|  29639|
|   CC BY-SA 2.5|2010-07-02T21:17:...|3260276|3169136|     3|And no info in Bo...|            null| 155356|
|   CC BY-SA 2.5|2010-07-02T21:17:...|3260277|3128496|     0|One thing to reme...|            null|  89761|
|   CC BY-SA 2.5|2010-07-02T21:17:...|3260279|3169068|     0|Not really relate...|            null|  74757|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260281|3168944|     0|javascript:var%20...|            null| 281705|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260282|3168667|     0|Yeah. But I think...|            null| 243943|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260283| 235067|     0|@Jon Skeet: Maybe...|            null| 135172|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260284|3161146|     0|This is a duplica...|            null| 340221|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260285|3161593|     0|Is the first_two_...|            null| 305555|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260286|3169115|     0|Isn't there an "E...|            null|  17028|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260287|3169126|     6|If your code is b...|            null| 189416|
|   CC BY-SA 2.5|2010-07-02T21:18:...|3260288|3169146|     2|Without code to e...|            null|  91768|
|   CC BY-SA 2.5|2010-07-02T21:19:...|3260289|3168175|     0|This is very nice...|            null| 312026|
|   CC BY-SA 2.5|2010-07-02T21:19:...|3260290|3167625|     0|I was able to fix...|            null|  87154|
|   CC BY-SA 2.5|2010-07-02T21:19:...|3260291|3163175|     0|The first solutio...|            null| 381675|
|   CC BY-SA 2.5|2010-07-02T21:19:...|3260292|3168299|     0|I think you can i...|            null|  69998|
|   CC BY-SA 2.5|2010-07-02T21:20:...|3260293| 204506|     0|@David Thornley -...|            null|   1737|
|   CC BY-SA 2.5|2010-07-02T21:20:...|3260294|3169159|     0|Is there somethin...|            null| 356292|
|   CC BY-SA 2.5|2010-07-02T21:20:...|3260295|3162018|     0|Okay what can i d...|            null| 365706|
+---------------+--------------------+-------+-------+------+--------------------+----------------+-------+
```



```
>>> spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet").show()
+--------------------+---------------+--------------------+---------+------------------+--------+--------------------+--------------------+----------------+-------+
|            _Comment|_ContentLicense|       _CreationDate|      _Id|_PostHistoryTypeId| _PostId|       _RevisionGUID|               _Text|_UserDisplayName|_UserId|
+--------------------+---------------+--------------------+---------+------------------+--------+--------------------+--------------------+----------------+-------+
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519365|                 5| 2613348|6499a078-4532-4d2...|When I went to Un...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519366|                 5| 2615297|26b49208-3be4-4eb...|If you have some ...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519367|                 5| 2619007|bc975e70-a69a-4f3...|How to create a s...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519368|                 5| 2617924|d529d0f4-15ed-4f1...|Yes - don't forge...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519369|                 5| 2617787|fb7ed36e-ee2b-42a...|Instead of nested...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519370|                 5| 2617507|bc1093c6-d4ca-435...|You said:  > ... ...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519371|                 5| 2617212|578031e6-c28a-4ff...|I am referred to ...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519372|                 5| 2617119|54556aab-9ea2-411...|i want get data f...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519373|                 5| 2616985|a600c321-4ab0-4c7...|Here is the issue...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519374|                 5| 2616839|0fb6470a-ca94-4d6...|The Wikipedia [Gr...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519375|                 5| 2616320|5db679ca-da0c-4ad...|I'm trying to cre...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519376|                 5| 2616314|301771e4-67a3-48c...|When defining you...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519377|                 5| 2616195|f81da27b-4153-49b...|This must be doab...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519378|                 5| 2618517|9ef29b6a-c1c3-432...|I'm racking my br...|            null|     -1|
|                null|   CC BY-SA 4.0|2020-06-20T09:45:...|224519379|                 2|62484164|11cc8566-d631-40a...|Your client code ...|            null| 256196|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519385|                 5| 2622179|1797efdd-e2fb-43e...|Sorry for answeri...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519386|                 5| 2621679|bc43b8a5-5d21-418...|With respect ther...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519387|                 5| 2621634|fcae8d6f-3af5-432...|From [Statement j...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519388|                 5| 2621174|59bb584d-129a-47c...|The general recur...|            null|     -1|
|Commonmark migration|   CC BY-SA 4.0|2020-06-20T09:12:...|224519389|                 5| 2621136|6f5e75ba-3413-4dc...|I have compiled t...|            null|     -1|
+--------------------+---------------+--------------------+---------+------------------+--------+--------------------+--------------------+----------------+-------+
```

```
>>> spark.read.parquet("/user/***REMOVED***/StackOverflow/PostLinks.parquet").show()
+--------------------+---+-----------+-------+--------------+
|       _CreationDate|_Id|_LinkTypeId|_PostId|_RelatedPostId|
+--------------------+---+-----------+-------+--------------+
|2010-04-26T02:59:...| 19|          1|    109|         32412|
|2010-04-26T02:59:...| 37|          1|   1970|        617600|
|2010-04-26T02:59:...| 42|          1|   2154|       2451138|
|2010-04-26T02:59:...| 52|          1|   2572|        209329|
|2010-04-26T02:59:...| 58|          1|   3376|          2187|
|2010-04-26T02:59:...| 59|          1|   3376|         18080|
|2010-04-26T02:59:...| 63|          1|   3859|        802573|
|2010-04-26T02:59:...| 69|          1|   4565|        583532|
|2010-04-26T02:59:...| 70|          1|   4582|       1955663|
|2010-04-26T02:59:...| 72|          1|   4850|       1369312|
|2010-04-26T02:59:...| 74|          1|   4952|          1607|
|2010-04-26T02:59:...| 75|          1|   4952|           173|
|2010-04-26T02:59:...| 76|          1|   4952|          6371|
|2010-04-26T02:59:...| 81|          1|   5724|        131955|
|2010-04-26T02:59:...| 84|          1|   6173|       1732348|
|2010-04-26T02:59:...| 90|          1|   7470|         82872|
|2010-04-26T02:59:...| 96|          1|   8170|        245395|
|2010-04-26T02:59:...|119|          1|   9705|        305694|
|2010-04-26T02:59:...|121|          1|   9751|           371|
|2010-04-26T02:59:...|126|          1|   9926|        619677|
+--------------------+---+-----------+-------+--------------+
```

```
>>> spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet").show()
+-----------------+------------+--------------------+-----------+-------------+-------------------+---------------+--------------------+--------------+------+--------------------+--------------------+----------------------+-----------------+-----------------+------------+---------+-----------+------+--------------------+--------------------+----------+
|_AcceptedAnswerId|_AnswerCount|               _Body|_ClosedDate|_CommentCount|_CommunityOwnedDate|_ContentLicense|       _CreationDate|_FavoriteCount|   _Id|   _LastActivityDate|       _LastEditDate|_LastEditorDisplayName|_LastEditorUserId|_OwnerDisplayName|_OwnerUserId|_ParentId|_PostTypeId|_Score|               _Tags|              _Title|_ViewCount|
+-----------------+------------+--------------------+-----------+-------------+-------------------+---------------+--------------------+--------------+------+--------------------+--------------------+----------------------+-----------------+-----------------+------------+---------+-----------+------+--------------------+--------------------+----------+
|             null|        null|<p>Have you tried...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:22:...|          null|821861|2009-05-06T13:38:...|2009-05-06T13:38:...|                  null|            95029|             null|       95029|   819238|          2|     2|                null|                null|      null|
|             null|        null|<p>It seems that ...|       null|            2|               null|   CC BY-SA 2.5|2009-05-04T20:22:...|          null|821862|2009-05-04T20:22:...|                null|                  null|             null|             null|       60315|   820218|          2|     0|                null|                null|      null|
|             null|        null|<blockquote> <p>F...|       null|            4|               null|   CC BY-SA 3.0|2009-05-04T20:23:...|          null|821864|2014-07-29T15:12:...|2020-06-20T09:12:...|                  null|               -1|             null|       55159|   311873|          2|     4|                null|                null|      null|
|             null|        null|<p>I would seriou...|       null|            2|               null|   CC BY-SA 2.5|2009-05-04T20:23:...|          null|821865|2009-05-04T21:43:...|2009-05-04T21:43:...|                  null|             2424|             null|        2424|   821598|          2|     1|                null|                null|      null|
|             null|        null|<pre><code>String...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:23:...|          null|821866|2009-05-04T20:23:...|                null|                  null|             null|             null|       89266|   821806|          2|     0|                null|                null|      null|
|           821986|           4|<p>Suppose I have...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:23:...|             2|821867|2009-05-08T07:18:...|2009-05-04T20:30:...|                  null|            16012|             null|       16012|     null|          1|     4|          <c#><linq>|how to process "p...|       640|
|             null|        null|<p>You have vario...|       null|            2|               null|   CC BY-SA 2.5|2009-05-04T20:23:...|          null|821868|2009-05-04T20:23:...|                null|                  null|             null|             null|       79294|   821780|          2|    10|                null|                null|      null|
|             null|        null|<p>Because that's...|       null|            1|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|          null|821869|2009-05-04T20:24:...|                null|                  null|             null|             null|       21886|   821839|          2|    20|                null|                null|      null|
|          1049025|           4|<p>I want to only...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|            40|821870|2017-05-09T10:09:...|                null|                  null|             null|             null|       36680|     null|          1|    26|<django><django-a...|How can I detect ...|     16019|
|             null|        null|<p>I had a deer-i...|       null|            2|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|          null|821871|2009-05-04T20:24:...|                null|                  null|             null|             null|      101116|   821740|          2|     0|                null|                null|      null|
|             null|        null|<p>Implement ISer...|       null|            1|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|          null|821872|2009-05-04T20:24:...|                null|                  null|             null|             null|       12971|   821780|          2|     2|                null|                null|      null|
|           822032|           7|<p>You wouldn't i...|       null|            2|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|             8|821873|2020-11-27T10:49:...|2009-05-04T20:56:...|                  null|            65336|             null|       65336|     null|          1|    57|<c++><windows><un...|How to open an st...|     57692|
|             null|        null|<p>On <strong>Lin...|       null|            7|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|          null|821874|2009-05-06T14:28:...|2009-05-06T14:28:...|                  null|            44434|             null|       44434|   821837|          2|    14|                null|                null|      null|
|             null|        null|<p>Interface prop...|       null|            2|               null|   CC BY-SA 2.5|2009-05-04T20:24:...|          null|821875|2009-05-04T20:24:...|                null|                  null|             null|             null|       16623|   821780|          2|    -1|                null|                null|      null|
|           822334|           4|<p>I've seen on s...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:25:...|             2|821877|2009-05-04T22:11:...|                null|                  null|             null|             null|      100884|     null|          1|     1|<php><web-applica...|Create a link bet...|       137|
|             null|        null|<p>The reason it ...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:25:...|          null|821879|2009-05-04T20:25:...|                null|                  null|             null|             null|       19131|   821839|          2|    12|                null|                null|      null|
|             null|        null|<p>Depending on y...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:25:...|          null|821881|2009-05-04T20:25:...|                null|                  null|             null|             null|       91872|   820807|          2|     5|                null|                null|      null|
|             null|        null|<p>One option is ...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:26:...|          null|821882|2009-05-04T20:40:...|2009-05-04T20:40:...|                  null|            41094|             null|       41094|   821844|          2|     8|                null|                null|      null|
|             null|        null|<p>Write a matrix...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:26:...|          null|821883|2009-05-04T20:26:...|                null|                  null|             null|             null|       32174|   819138|          2|    16|                null|                null|      null|
|             null|        null|<p>Convert the tw...|       null|            0|               null|   CC BY-SA 2.5|2009-05-04T20:26:...|          null|821884|2009-05-04T20:26:...|                null|                  null|             null|             null|       78259|   821423|          2|     1|                null|                null|      null|
+-----------------+------------+--------------------+-----------+-------------+-------------------+---------------+--------------------+--------------+------+--------------------+--------------------+----------------------+-----------------+-----------------+------------+---------+-----------+------+--------------------+--------------------+----------+
```

```
>>> spark.read.parquet("/user/***REMOVED***/StackOverflow/Tags.parquet").show()
+-------+--------------+---+----------+-----------+
| _Count|_ExcerptPostId|_Id|  _TagName|_WikiPostId|
+-------+--------------+---+----------+-----------+
| 303362|       3624959|  1|      .net|    3607476|
|1038358|       3673183|  2|      html|    3673182|
|2130783|       3624960|  3|javascript|    3607052|
| 694921|       3644670|  4|       css|    3644669|
|1381623|       3624936|  5|       php|    3607050|
| 345968|       3624961|  8|         c|    3607013|
|1450818|       3624962|  9|        c#|    3607007|
| 702947|       3624963| 10|       c++|    3606997|
| 216766|       3624964| 12|      ruby|    3607043|
|   6324|       3656743| 14|      lisp|    3656742|
|1597896|       3624965| 16|    python|    3607014|
|1735439|       3624966| 17|      java|    3607018|
| 235211|       3624967| 18|     regex|    3607017|
| 198437|       3624968| 19|       xml|    3607588|
| 613118|       3624969| 21|     mysql|    3607033|
| 570524|       3625226| 22|       sql|    3607304|
|  64654|       4777787| 23|      tsql|    4777786|
|     63|       8355939| 26|        j#|    8355938|
|  24176|       5388160| 27|   browser|    5388159|
|  80168|       4890031| 28|      linq|    4890030|
+-------+--------------+---+----------+-----------+
```