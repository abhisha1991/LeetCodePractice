using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class Program
    {
      
        static void Main(string[] args)
        {
            GameOfLife.GameOfLifeMain();
            ParseHtml.ParseHtmlMain(null);
            AllTextSuggestions.AllTextSuggestionsMain(null);
            BSTIteratorDriver.BSTIteratorMain(null);
            TopologicalSort.TopologicalSortMain();
            Prims.PrimsMain(null);
            Kruskals.KruskalsMain(null);
            WordSearch.wordSearchMain();
            CountSmallerAfterNumber2.CountSmallerAfterNumber2Main();
            CountSmallerAfterNumber.countSmallerMain();
            BFS.BFSMain(null);
            StringPermutation.StringPermutationMain(); // Done
            RemoveKFromList.RemoveKFromListMain();
            TripletSum.tripletSumMain();
            SubsetSum.subsetSumMain();
            RotateImage.rotateImageMain(); // Done
            StrStr.strStrMain(); // Done - exceeding time
            SumOfTwo.SumOfTwoMain(); // Not done
            SortedSquaredArray.sortedSquaredArrayMain(); // Done
            IsListPalindrome.isListPalindromeMain(); // Done
            SwapLexOrder.swapLexOrderMain();
            TextJustification.textJustificationMain(); // Done
            GoodStringCount.goodStringsCountMain(); // Not done
            WordLadder.wordLadderMain(); // Not complete by me
            SortingAlgos.sortingAlgosMain(); // Done
            SortByString.sortByStringMain(); // Done
            StringReformatting.stringReformattingMain(); // Done
            ReverseInteger.reverseIntegerMain(); // Done
            ProductExceptSelf.productExceptSelfMain(); // Done
        }
      
    }
}
