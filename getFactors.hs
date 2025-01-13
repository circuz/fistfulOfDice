import System.Environment (getArgs)

main :: IO ()
main = do
  args <- getArgs
  let g = read (head args)
  putStrLn $ (show g) ++ "> " ++  (show . getFactors $ g)


getFactors :: Integer -> [Integer]
getFactors 1 = []
getFactors x = do
  let f = getSmallestFactor 2 x
  case f of
    -1 -> [x]
    _ -> [f] ++ getFactors (div x f)

getSmallestFactor :: Integer -> Integer -> Integer
getSmallestFactor x y = case (>) (x*x) y of
  True -> -1
  False -> case mod y x of
    0 -> x
    _ -> getSmallestFactor (x+1) y

