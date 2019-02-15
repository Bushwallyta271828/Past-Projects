(reset-meep)

(define (show text)
	(display text)
	(newline)
)

(define (make-blocks ys sax is sox os xtot ytot mater thick pm);ys = points
							       ;sax = startx
							       ;is = in-size
							       ;sox = stopx
							       ;os = out-size
					   		       ;xtot = x
						 	       ;ytot = y
							       ;mater = mat
	    						       ;thick = width-
							       ;pm means top or bottom. pm = 1 means make the top line. pm = -1 means make the bottom line.
							       ;returns a list of blocks.
	(define scale (/ (- is os) 2))
	(if (null? ys)
		(list (make block (center (/ (+ xtot (* 2 sox)) 4) 
					  (* pm (/ (+ os thick) 2))
				  )
				  (size (/ (- xtot (* 2 sox)) 2)
					thick
				  )
				  (material mater)
		      )
		)
		(if (= (length ys) 1)
			(cons
				(make block (center (+ sax 
						       (/ (- sox sax) (* 2 (length ys)))
						    )
						    (* pm 
						       (+ (/ thick 2)
							  (/ (+ (/ os 2)
								(+ (/ os 2) (* scale (car ys)))
							     )
							     2
							  )
						       )
						    )
					    )
					    (size (sqrt (+ (expt (/ (- sox sax) (length ys))
								 2
							   )
							   (expt (* scale (car ys))
								 2
							   )
							)
						  )
						  thick
					    )
					    (e1 (/ (- sox sax) (length ys))
						(* pm scale (- (car ys)))
					    )
					    (e2 0 thick)
					    (material mater)
				)
				(make-blocks (cdr ys)
						(+ sax
						   (/ (- sox sax) (length ys))
						)
						is sox os xtot ytot mater thick pm
				)
			)
			(cons
				(make block (center (+ sax
						       (/ (- sox sax) (* 2 (length ys)))
						    ) 
						    (* pm
						       (+ (/ thick 2) 
							  (/ (+ (+ (/ os 2) (* scale (cadr ys)))
			   					(+ (/ os 2) (* scale (car ys)))
							     )
							     2
							  )
						       )
						    )
				    	    )
					    (size (sqrt (+ (expt (/ (- sox sax) (length ys))
								 2
							   )
							   (expt (-  (* scale (car ys))
								     (* scale (cadr ys)) 
								 )
								 2
							   )
							)
						  )
						  thick
					    )
					    (e1 (/ (- sox sax) (length ys))
						(* pm
						   (- (* scale (cadr ys))
						      (* scale (car ys))
						   )
						)
					    )
					    (e2 0 thick)
					    (material mater)
		       		)
				(make-blocks (cdr ys)
						(+ sax 
						   (/ (- sox sax) (length ys))
						)
						is sox os xtot ytot mater thick pm
				)
			)
		)
	)
)

(define (make-funnel ys sax is sox os xtot ytot mater thick);ys = points
	 						    ;sax = startx
							    ;is = in-size
							    ;sox = stopx
							    ;os = out-size
							    ;xtot = x
							    ;ytot = y
							    ;mater = mat
							    ;thick = width-
							    ;returns all the boxes in a big ugly pile, ready to be smashed with blinding radio waves.
	(append (list (make block (center (/ (- (* 2 sax) xtot) 4)
					  (/ (+ is thick) 2)
				  )
				  (size (+ sax (/ xtot 2))
					thick
				  )
				  (material mater)
		      )
		)
		(make-blocks (cons 1 ys) sax is sox os xtot ytot mater thick 1)
		(list (make block (center (/ (- (* 2 sax) xtot) 4)
					  (* -1 (/ (+ is thick) 2))
				  )
				  (size (+ sax (/ xtot 2))
					thick
				  )
				  (material mater)
		      )
		)
		(make-blocks (cons 1 ys) sax is sox os xtot ytot mater thick -1)
	)
)

(define-param points (list 1.0 0.982658087111 0.957895251106 0.900551508061 0.812570276832 0.716803628769 0.670939502062 0.515313961376 0.516440824352 0.365352112277)) ;These are the coordinates of the vertices.
(define-param startx -1.5) ;This is the start of the funnel.
(define-param in-size 1) ;This is the width of the funnel's entrance.
(define-param stopx 1.6) ;This is the stop of the funnel.
(define-param out-size 0.1) ;This is the width of the funnel's exit.
(define-param x 4) ;This is the x-width of the computational domain.
(define-param y 2) ;This is the y-width of the computational domain.
(define-param mat (make medium (epsilon (expt 10 6)))) ;This is the material the blocks will be made from.
(define-param width- 0.4) ;This is the vertical thickness of the walls.
(define-param res 75) ;This is the resolution of the grid.
(define-param freq 3) ;This is the frequency of the waves entering the funnel.
(define-param pml-thickness- 0.01) ;This is the thickness of the pml.


(set! geometry-lattice (make lattice (size x y no-size))) ;We make the lattice
(set! geometry (make-funnel points startx in-size stopx out-size x y mat width-)) ;We set the geometry using our pre-defined functions
(set! resolution res) ;We set the resolution
(set! symmetries (list (make mirror-sym (direction Y)))) ;We set the symmetries
(set! sources (list (make source (src (make continuous-src (frequency freq)))
				 (component Ex) ;We're generating electric field in the x direction
				 (center (+ (- (/ x 2)) (/ (+ startx (/ x 2)) 6))
					 0
				 );This is the center of the source
				 (size (/ (+ startx (/ x 2)) 6)
				       in-size
				 );These are the dimensions of the source
		    )
	      )
)

(define-param in-box (volume (center (/ (+ (- x) (* 4 startx)) 6) 0)
			     (size (/ (+ startx (/ x 2)) 3) in-size)
		     )
) ;This is the volume where we will measure the energy near the source.
(define-param out-box (volume (center (/ (+ x (* 2 stopx)) 4) 0)
			      (size (/ (- x (* 2 stopx)) 4) out-size)
		      )
) ;This is the volume where we will measure the energy near the exit.
(define-param avg-length 100) ;We average sum over the last avg-length terms to find the ratio.



(define (lasts n l)
	(if (= n 1)
		(list (car l))
		(cons (car l)
		      (lasts (- n 1) (cdr l))
		)
	)
) ;This returns the first n items of l

(define (sum to-sum)
	(if (null? to-sum)
		0
		(+ (car to-sum)
		   (sum (cdr to-sum))
		)
	)
) ;This returns the sum of to-sum

(define (func)
	(set! ins (cons (/ (field-energy-in-box in-box)
			   (* (/ (+ startx (/ x 2)) 3)
			      in-size
			   )
			)
			ins
		  )
	)
	(set! outs (cons (/ (field-energy-in-box out-box)
			    (* (/ (- x (* 2 stopx)) 4)
			       out-size
			    )
			 )
			 outs
		   )
	)
)

(init-fields)
(set! pml-layers (list (make pml (thickness pml-thickness-))))
(define-param ins (list 0))
(define-param outs (list 0))
(run-until 50
	func
)
(define ratio (/ (sum (lasts avg-length outs))
   	         (sum (lasts avg-length ins))
	      )
)
(show ratio)
