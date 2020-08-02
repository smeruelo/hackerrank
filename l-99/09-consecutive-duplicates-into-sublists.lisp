(defun dup-sublists (lst)
  (defun aux (done current pending)
    (if (null pending)
        (reverse done)
        (if (eql (car pending) (cadr pending))
            (aux done
                 (cons (car pending) current)
                 (cdr pending))
            (aux (cons (cons (car pending) current) done)
                 ()
                 (cdr pending)))))
  (aux () () lst))
