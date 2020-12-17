from pyspark.sql import SparkSession
from pyspark.sql.functions import array, array_intersect, col, expr, lit, size, split, when


def tag_info_df(spark):
    """ Extract features from the tags of a post

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [(post)_Id, number_of_tags, contains_language_tag, contains_platform_tag]
    """
    language_list = ["abap", "abc", "actionscript", "ada", "algol", "algol 58", "algol 60", "algol w", "algol 68", "alice", "amiga e", "apex", "apl", "applescript", "argh!", "aargh!", "assembly", "assembly language", "autolisp", "autolt", "awk",
                     "b", "bash", "basic", "ballerina", "bbc basic", "bc", "bcpl", "blitz basic", "bourne shell", "brainfuck",
                     "c", "c++", "c#", "cfml", "cl", "classic visual basic", "clean", "clipper", "clojure", "cobol", "comal", "common lisp", "coffeescript", "crystal", "c shell", "ct",
                     "d", "darkbasic", "dart", "decimal basic", "delphi", "delta cobol", "div games studio",
                     "egl", "eiffel", "elixir", "elm", "emacs lisp", "erlang", "euphoria",
                     "f#", "factor", "fenix project", "forth", "fortran", "foxpro",
                     "gambas", "gcl", "gml", "go", "grasshopper", "groovy",
                     "hack", "haskell", "hypertalk",
                     "icon", "inform", "io", "ironpython",
                     "j", "just another language", "java", "javascript", "just basic", "jscript", "julia",
                     "korn shell", "kotlin",
                     "labview", "ladder logic", "leet", "liberty basic", "lisp", "logo", "lua",
                     "m4", "machine", "machine language", "malbolge", "maple", "matlab", "m-code", "mercury", "ml", "modula-2", "mondrian", "mql4", "msl",
                     "natural",
                     "oberon", "objective-c", "objectpal", "object pascal", "ocaml", "opencl", "openedge abl", "oz",
                     "pascal", "pawn", "perl", "php", "piet", "pl/1", "pl/i", "pl/sql", "pl/pgsql", "postscript", "powerbasic", "powerbuilder", "powershell", "processing", "progress", "prolog", "providex", "purebasic", "python",
                     "q#", "qbasic",
                     "r", "raku", "rexx", "ring", "rpg", "ruby", "rust",
                     "sas", "scala", "sed", "scheme", "scratch", "scratch jr.", "seed7", "self", "simula", "smalltalk", "smallbasic", "snobol", "solidity", "spark", "spss", "sql", "stata", "swift",
                     "tcl", "tex", "ti-basic", "transact-sql", "t-sql", "turbobasic", "turbo c", "turbo pascal", "typescript",
                     "ubasic",
                     "vala", "vala/genie", "vb", "vbs", "vbscript", "verilog", "vhdl", "visual basic", "visual c", "visual foxpro", "visual objects", "vbscripts", "whitespace",
                     "xslt", "xquery",
                     "yaml"]
    language_list_col = array(*[lit(x) for x in language_list])
    platform_list = ["windows", "linux", "maccie"]
    platform_list_col = array(*[lit(x) for x in platform_list])

    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_Tags"]) \
        .withColumn("_Tags", expr("substring(_Tags, 2, length(_Tags) - 2)")) \
        .withColumn("_Tags", split(col("_Tags"), "><")) \
        .withColumn("number_of_tags", when(size("_Tags") < 0, 0).otherwise(size("_Tags"))) \
        .withColumn("contains_language_tag", size(array_intersect("_Tags", language_list_col)) > 0) \
        .withColumn("contains_platform_tag", size(array_intersect("_Tags", platform_list_col)) > 0) \
        .drop("_Tags")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    tag_info_df(spark).show()
