#lang racket
(include "hw3pr5_range.rkt")
(require rackunit)
(require (prefix-in rackUnit: rackunit/text-ui))


(define file-tests
  (test-suite
   "tests"
    (check-equal? (value1to3? 0)  #f
                  "(value1to3 0)")
    (check-equal? (value1to3? 1)  #t
                  "(value1to3 1)")
    (check-equal? (value1to3? 2)  #t
                  "(value1to3 2)")
    (check-equal? (value1to3? 3)  #t
                  "(value1to3 3)")
    (check-equal? (value1to3? 4)  #f
                  "(value1to3 4)")
    (check-equal? (value1to3? 42) #f
                  "(value1to3 42)")

    (check-equal? (value1to100? 0)   #f
                  "(value1to100 0)")
    (check-equal? (value1to100? 1)   #t
                  "(value1to100 1)")
    (check-equal? (value1to100? 20)  #t
                  "(value1to100 20)")
    (check-equal? (value1to100? 42)  #t
                  "(value1to100 42)")
    (check-equal? (value1to100? 100) #t
                  "(value1to100 100)")
    (check-equal? (value1to100? 101) #f
                  "(value1to100 101)")
    (check-equal? (value1to100? 999) #f
                  "(value1to100 999)")
  )
)

(rackUnit:run-tests file-tests 'normal)   