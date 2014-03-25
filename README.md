A parser for the GEIZELA language


The grammar is as follows

	atty ::== tyid			type identifier
		  '(tyseq)		tuple type
		  '{tyrow}		record type
		  &atty			reference type
		  @atty			array type
		  (ty)

	ty   ::== atty
		  atty -> ty		function type : one argument
		  (tyseq) ->ty		function type : multiple arguments

	tyseq::== E
		  ty{,ty}		type sequence

	tyrow::== E
		  lab : ty {,lab : ty}	type row
