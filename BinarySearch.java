public class BinarySearch {
    public int search(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        int mid;

        while (lo <= hi) {
            mid = (lo + hi) / 2;
            if (target < nums[mid]) {
                hi = mid - 1;
            }
            else if (nums[mid] < target) {
                lo = mid + 1;
            }
            else {
                return mid;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        BinarySearch bs = new BinarySearch();

        // Test case 1, element is in the array:
        int[] nums1 = {-5, 1, 3, 6, 8};
        int target1 = 3;
        int expected1 = 2; // index of 3 in nums1
        System.out.println("Test 1 Passed: " + (bs.search(nums1, target1) == expected1));

        // Test case 2, element is not in the array:
        int target2 = 7;
        int expected2 = -1; // since 7 is not in nums1
        System.out.println("Test 2 Passed: " + (bs.search(nums1, target2) == expected2));

        // Test case 3, empty array:
        int[] nums3 = {};
        int target3 = 3;
        int expected3 = -1; // since array is empty
        System.out.println("Test 3 Passed: " + (bs.search(nums3, target3) == expected3));

        // Test case 4, single-element array, target is present:
        int[] nums4 = {3};
        int target4 = 3;
        int expected4 = 0; // index of 3 in nums4
        System.out.println("Test 4 Passed: " + (bs.search(nums4, target4) == expected4));

        // Test case 5, single-element array, target is not present:
        int target5 = 1;
        int expected5 = -1; // since 1 is not in nums4
        System.out.println("Test 5 Passed: " + (bs.search(nums4, target5) == expected5));

        // Test case 6, searching for the first and last elements:
        int[] nums6 = {-10, -5, 0, 5, 10};
        System.out.println("Test 6.1 Passed: " + (bs.search(nums6, -10) == 0)); // First element
        System.out.println("Test 6.2 Passed: " + (bs.search(nums6, 10) == 4));  // Last element
    }
}